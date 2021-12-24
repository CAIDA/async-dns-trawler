import json
from typing import List, Optional, Set

import pydgraph
from pydgraph.proto.api_pb2 import Response as PyDgraphResponse

from dt.client.dgraph.client.server_address import ServerAddress
from dt.client.dgraph.constants.builtin_predicate import BuiltinPredicate
from dt.client.dgraph.constants.comparison_function import ComparisonFunction
from dt.client.dgraph.constants.mutation_type import MutationType
from dt.client.dgraph.constants.schema_attribute_type import \
    SchemaAttributeType
from dt.client.dgraph.dql.anonymous_argument import AnonymousArgument
from dt.client.dgraph.dql.dgraph_schema import DGraphSchema
from dt.client.dgraph.dql.dql_variable_set import DQLVariableSet
from dt.client.dgraph.dql.query_function import QueryFunction
from dt.client.dgraph.dql.query_operation import QueryOperation
from dt.client.dgraph.dql.query_root import QueryRoot
from dt.client.dgraph.entity.blank_node import BlankNode
from dt.client.dgraph.entity.node import Node
from dt.client.dgraph.entity.transaction import Transaction
from dt.client.dgraph.error.mutation_error import MutationError
from dt.client.dgraph.graphql.field import Field
from dt.client.dgraph.graphql.graphql import GraphQL
from dt.client.dgraph.graphql.selection_set import SelectionSet
from dt.client.dgraph.graphql.value import Value
from dt.client.dgraph.graphql.variable import Variable
from dt.client.dgraph.mapper.attribute_predicate_mapper import \
    AttributePredicateMapper
from dt.client.dgraph.mapper.query_expression_mapper import \
    QueryExpressionMapper
from dt.dns_trawler.constants.sort_direction import SortDirection
from dt.dns_trawler.db.i_database_client import IDatabaseClient
from dt.dns_trawler.db.query_options import QueryOptions
from dt.dns_trawler.db.query_response import QueryResponse
from dt.dns_trawler.error.internal_server_error import InternalServerError
from dt.dns_trawler.error.resource_already_exists_error import \
    ResourceAlreadyExistsError
from dt.dns_trawler.error.resource_not_found_error import ResourceNotFoundError
from dt.dns_trawler.error.validation_error import ValidationError

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
        query_root = QueryRoot(func=QueryFunction(
            ComparisonFunction.UID, (uid_variable.get_reference(),)
        ))
        node_list = self._query(query_root=query_root, variables=variables)
        # DGraph UID function acts as identity function in cases where
        # the reference node doesn't exist. In those cases, the returned
        # dictionary will have a single key containing the queried UID
        if len(node_list) != 1 or len(node_list[0].predicates) == 0:
            message = f"Node: {node_id} does not exist in the database"
            raise ResourceNotFoundError(message)
        node = node_list[0]
        return node

    def create(self, node: Node) -> Node:
        ''' Create a node in the database
        Args:
            node: The node to create in the database
        Returns:
            The created node
        Raises:
            ResourceAlreadyExistsError if the node already exists in the
                database
            ValidationError: if the returned response does not contain
                             all required field
            InternalServerError: if the mutation fails
        '''
        node_id = node.uid.value
        retrieved_node = self._get_if_exists(node)
        if retrieved_node is not None:
            message = f"Node: {node_id} already exists in the database"
            raise ResourceAlreadyExistsError(message)
        try:
            res = self._mutate(node, MutationType.STORE)
        except MutationError as err:
            message = f"Unable to create node: {node} in database"
            raise InternalServerError(message) from err
        new_node_id = node_id
        if isinstance(node, BlankNode):
            if node_id not in res.uids:
                message = f"Invalid response when creating node: {node}"
                raise ValidationError(message)
            new_node_id = res.uids[node_id]
        key_node = Node(new_node_id)
        created_node = self.get(key_node)
        return created_node

    def update(self, node: Node) -> Node:
        ''' Update a node in the database
        Args:
            node: The node to update
        Returns:
            The updated node
        Raises:
            ResourceNotFoundError if the node to update does not
                exist in the database
            InternalServerError: if the mutation fails
        '''
        retrieved_node = self._get_if_exists(node)
        if retrieved_node is None:
            message = f"Node: {node.uid.value} does not exist in the database"
            raise ResourceNotFoundError(message)
        try:
            self._mutate(node, MutationType.STORE)
        except MutationError:
            message = f"Unable to update node: {node} in database"
            raise InternalServerError(message)
        return self.get(node)

    def delete(self, node: Node) -> None:
        ''' Delete an node from the database
        Args:
            item: The resource to delete
        Raises:
            InternalServerError: if the mutation fails
        '''
        retrieved_node = self._get_if_exists(node)
        if retrieved_node is not None:
            try:
                self._mutate(retrieved_node, MutationType.DELETE)
            except MutationError:
                message = f"Unable to delete node: {node} in database"
                raise InternalServerError(message)

    def query(self, query_options: QueryOptions) -> QueryResponse[Node]:
        ''' Retrieve a list of nodes from the database that match a
            certain query
        Args:
            query_options: Config for the query
        Returns:
            A list of nodes matching the query
        Raises:
            InternalServerError: if the query fails
        '''
        func = QueryExpressionMapper.to_query_function(query_options.expression)
        query_root = QueryRoot(func)
        if query_options.max_results:
            query_root.first = query_options.max_results
        if query_options.next_token:
            query_root.after = query_options.next_token
        if query_options.order_by:
            field_name = query_options.order_by.query_field.field_name
            if query_options.order_by.sort_direction == SortDirection.ASC:
                query_root.orderasc = field_name
            else:
                query_root.orderdesc = field_name
        node_list = self._query(query_root=query_root)
        next_token = None
        if query_options.max_results and len(node_list) > 0:
            final_node = node_list[-1]
            next_token = final_node.uid.value
        query_response = QueryResponse(items=node_list, next_token=next_token)
        return query_response

    def _query(self, query_root: QueryRoot, variables: Optional[DQLVariableSet] = None) -> List[Node]:
        uid_field = Field(name=_UID_FIELD_NAME)
        expand_field = Field(
            name=_EXPAND_FIELD_NAME,
            arguments={AnonymousArgument(Value(BuiltinPredicate.ALL))},
            selection_set=SelectionSet(uid_field)
        )
        query_operation = QueryOperation(
            name=_GET_OPERATION_NAME,
            variables=variables,
            query_root=query_root,
            selection_set=SelectionSet(uid_field, expand_field)
        )
        get_query = GraphQL(query_operation)
        txn = self._client.txn(read_only=True)
        try:
            variable_dict = None
            if variables:
                variable_dict = variables.get_value_dict()
            res = txn.query(get_query, variables=variable_dict)
        except BaseException as err:
            message = f"Unable to perform query: {get_query}"
            raise InternalServerError(message) from err
        finally:
            txn.discard()
        data = json.loads(res.json)[_GET_OPERATION_NAME]
        node_list = []
        for node_data in data:
            if _UID_FIELD_NAME not in node_data:
                raise ValidationError(f"Unable to parse response: {node_data}")
            node_id = node_data[_UID_FIELD_NAME]
            node = Node(node_id)
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
            node_list.append(node)
        return node_list

    def _mutate(self, node: Node, mutation_type: MutationType) -> PyDgraphResponse:
        transaction = Transaction({node})
        txn = self._client.txn()
        try:
            nquad_str = transaction.to_dql_triples().to_nquad_statement()
            if mutation_type == MutationType.STORE:
                res = txn.mutate(set_nquads=nquad_str)
            elif mutation_type == MutationType.DELETE:
                res = txn.mutate(del_nquads=nquad_str)
            else:
                message = f"Mutation of type: {mutation_type} is not supported."
                raise MutationError(message)
        except BaseException as err:
            message = f"Unable to mutate database for node: {node}"
            raise MutationError(message) from err
        finally:
            txn.discard()
        return res

    def _get_if_exists(self, node: Node) -> Optional[Node]:
        try:
            returned_node = self.get(node)
            return returned_node
        except ResourceNotFoundError:
            return None
