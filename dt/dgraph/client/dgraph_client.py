import json
from typing import List, Set

import pydgraph

from dt.dgraph.client.server_address import ServerAddress
from dt.dgraph.constants.builtin_predicate import BuiltinPredicate
from dt.dgraph.constants.comparison_function import ComparisonFunction
from dt.dgraph.constants.graphql_operation import GraphQLOperation
from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.dql.anonymous_argument import AnonymousArgument
from dt.dgraph.dql.dgraph_schema import DGraphSchema
from dt.dgraph.dql.dql_variable_set import DQLVariableSet
from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.node_schema import NodeSchema
from dt.dgraph.dql.query_function import QueryFunction
from dt.dgraph.dql.query_operation import QueryOperation
from dt.dgraph.dql.query_root import QueryRoot
from dt.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.dgraph.entity.node import Node
from dt.dgraph.entity.transaction import Transaction
from dt.dgraph.graphql.argument import Argument
from dt.dgraph.graphql.field import Field
from dt.dgraph.graphql.graphql import GraphQL
from dt.dgraph.graphql.selection_set import SelectionSet
from dt.dgraph.graphql.value import Value
from dt.dgraph.graphql.variable import Variable
from dt.dgraph.mapper.attribute_predicate_mapper import \
    AttributePredicateMapper
from dt.dns_trawler.db.i_database_client import IDatabaseClient
from dt.dns_trawler.db.query_options import QueryOptions
from dt.dns_trawler.error.internal_server_error import InternalServerError
from dt.dns_trawler.error.resource_already_exists_error import \
    ResourceAlreadyExistsError
from dt.dns_trawler.error.resource_not_found_error import ResourceNotFoundError

_GET_OPERATION_NAME = "get"
_UID_FIELD_NAME = "uid"
_EXPAND_FIELD_NAME = "expand"
_UID_VARIABLE_NAME = "uid"
_STRING_ATTRIBUTE_TYPE = SchemaAttributeType.STRING.value


class DGraphClient(IDatabaseClient[Node]):
    ''' Represent a queryable connection to a DGraph database

    hosts: Set of server addresses the client is connected to
    _client_stubs: List of PyDGraph client stubs for each server address
    _client: Underlying PyDGraph client
    '''

    def __init__(self, hosts: Set[ServerAddress], dgraph_schema: DGraphSchema):
        self.hosts = hosts
        self._client_stubs = [pydgraph.DgraphClientStub(server_address.get_address()) for server_address in hosts]
        self._client = pydgraph.DgraphClient(*self._client_stubs)
        self.dgraph_schema = dgraph_schema

    def close(self) -> None:
        for stub in self._client_stubs:
            stub.close()

    def set_schema(self, dgraph_schema: DGraphSchema) -> None:
        schema_str = dgraph_schema.to_schema_statement()
        schema_operation = pydgraph.Operation(schema=schema_str)
        self._client.alter(schema_operation)
        self.dgraph_schema = dgraph_schema

    def get(self, key: Node) -> Node:
        ''' Retrieves a full node given a sparse key node
        Args:
            key: A node containing at minimum the uid to query for. This
                 must not be a blank node.
        Returns:
            A node with the data retrieved from the database
        Raises:
            ResourceNotFoundError if the queried node does not exist
                or if the queried node references an unknown schema
                attribute
            InternalServerError if the query fails

        '''
        node_id = key.uid.value
        uid_variable = Variable(name=_UID_VARIABLE_NAME,
                                variable_type=_STRING_ATTRIBUTE_TYPE,
                                value=Value(node_id))
        variables = DQLVariableSet(uid_variable)
        uid_field = Field(name=_UID_FIELD_NAME)
        expand_field = Field(
            name=_EXPAND_FIELD_NAME,
            arguments={AnonymousArgument(Value(BuiltinPredicate.ALL))},
            selection_set=SelectionSet(uid_field)
        )
        query_operation = QueryOperation(
            name=_GET_OPERATION_NAME,
            variables=variables,
            query_root=QueryRoot(func=QueryFunction(
                ComparisonFunction.UID, (uid_variable.get_reference(),)
            )),
            selection_set=SelectionSet(uid_field, expand_field)
        )
        get_query = GraphQL(query_operation)
        txn = self._client.txn(read_only=True)
        try:
            res = txn.query(get_query, variables=variables.get_value_dict())
        except BaseException:
            message = f"Unable to query for node: {node_id}"
            raise InternalServerError(message)
        finally:
            txn.discard()
        data = json.loads(res.json)[_GET_OPERATION_NAME]
        # DGraph UID function acts as identity function in cases where
        # the reference node doesn't exist. In those cases, the returned
        # dictionary will have a single key containing the queried UID
        if len(data) == 0 or len(data[0]) == 1:
            message = f"Node: {node_id} does not exist"
            raise ResourceNotFoundError(message)
        node = Node(node_id)
        node_data = data[0]
        schema_attribute_dict = self.dgraph_schema.get_attribute_dict()
        for attr_name, attr_value in node_data.items():
            if attr_name != _UID_FIELD_NAME:
                if attr_name not in schema_attribute_dict:
                    message = f"Attribute with name: {attr_name} not found in client schema"
                    raise ResourceNotFoundError(message)
                attribute = schema_attribute_dict[attr_name]
                if attribute.is_list_type:
                    for item in attr_value:
                        predicate = AttributePredicateMapper.to_predicate(attribute, item)
                        node.add_predicate(predicate)
                else:
                    predicate = AttributePredicateMapper.to_predicate(attribute, attr_value)
                    node.add_predicate(predicate)
        return node

    def create(self, node: Node) -> Node:
        node_id = node.uid.value
        node_exists = True
        try:
            self.get(node)
        except ResourceNotFoundError:
            node_exists = False
        if node_exists:
            message = f"Node: {node_id} already exist in the database"
            raise ResourceAlreadyExistsError(message)
        transaction = Transaction({node})
        txn = self._client.txn()
        try:
            nquad_str = transaction.to_dql_triples().to_nquad_statement()
            res = txn.mutate(set_nquads=nquad_str)
        except BaseException:
            message = f"Unable to create node: {node}"
            raise InternalServerError(message)
        finally:
            txn.discard()

    def update(self, node: Node) -> Node:
        transaction = Transaction({node})
        txn = self._client.txn()
        try:
            nquad_str = transaction.to_dql_triples().to_nquad_statement()
            res = txn.mutate(set_nquads=nquad_str)
        except BaseException:
            message = f"Unable to put node: {node}"
            raise InternalServerError(message)
        finally:
            txn.discard()
        return node

    def delete(self, node: Node) -> None:
        pass

    def query(self, query_options: QueryOptions) -> List[Node]:
        pass
