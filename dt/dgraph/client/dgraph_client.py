from typing import Set
import json

import pydgraph

from dt.dgraph.client.server_address import ServerAddress
from dt.dgraph.client.transaction import Transaction
from dt.dgraph.dql.dgraph_schema import DGraphSchema
from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.node_schema import NodeSchema
from dt.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.dgraph.entity.node import Node
from dt.dgraph.error.internal_server_error import InternalServerError
from dt.dgraph.error.resource_not_found_error import ResourceNotFoundError
from dt.dgraph.mapper.attribute_predicate_mapper import AttributePredicateMapper

class DGraphClient:
    ''' Represent a queryable connection to a DGraph database 
    
    hosts: Set of server addresses the client is connected to
    _client_stubs: List of PyDGraph client stubs for each server address
    _client: Underlying PyDGraph client
    '''

    def __init__(self, hosts=Set[ServerAddress]):
        self.hosts = hosts
        self._client_stubs = [pydgraph.DgraphClientStub(server_address.get_address()) for server_address in hosts]
        self._client = pydgraph.DgraphClient(*self._client_stubs)

    def set_schema(self, dgraph_schema:DGraphSchema) -> None:
        schema_str = dgraph_schema.to_schema_statement()
        schema_operation = pydgraph.Operation(schema=schema_str)
        self._client.alter(schema_operation)

    def get(self, node_id:NodeId, node_schema:NodeSchema) -> Node:
        get_query = "query target($uid: string) {\n" + \
                    "target(func: uid($uid)) {\n" + \
                    "expand(__all__) {\n" + \
                    "uid\n" + \
                    "} } }"
        variables = {'$uid': node_id.value}
        node = Node(node_id)
        txn = self._client.txn(read_only=True)
        try:
            res = txn.query(get_query, variables=variables)
        except:
            message = f"Unable to query for node: {node_id} of type {node_schema.node_type}"
            raise InternalServerError(message)
        finally:
            txn.discard()
        data = json.loads(res.json)['target']
        if len(data) == 0:
            message = f"Node: {node_id} does not exist"
            raise ResourceNotFoundError(message)
        node_data = data[0]
        for attribute in node_schema.get_attributes():
            attr_name = attribute.attr_name
            if attr_name in node_data:
                if attribute.is_list_type:
                    for value in node_data[attr_name]:
                        predicate = AttributePredicateMapper.to_predicate(attribute, value)
                        node.add_predicate(predicate)
                else:
                    value = node_data[attr_name]
                    predicate = AttributePredicateMapper.to_predicate(attribute, value)
                    node.add_predicate(predicate)
        return node

    def put(self, node:Node) -> Node:
        transaction = Transaction({node})
        txn = self._client.txn()
        try:
            nquad_str = transaction.to_nquad_statement()
            txn.mutate(set_nquads=nquad_str)
        except:
            message = f"Unable to put node: {node}"
            raise InternalServerError(message)
        finally:
            txn.discard()
        return node