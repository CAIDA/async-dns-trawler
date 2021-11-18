import unittest
from unittest.mock import patch, MagicMock

import pydgraph
from pydgraph.errors import AbortedError

from dt.dgraph.client.server_address import ServerAddress
from dt.dgraph.client.dgraph_client import DGraphClient
from dt.dgraph.constants.index_type import StringIndex
from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.dql.dgraph_schema import DGraphSchema
from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.node_schema import NodeSchema
from dt.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.dgraph.dql.type_attribute import TypeAttribute
from dt.dgraph.entity.node import Node
from dt.dgraph.error.internal_server_error import InternalServerError
from dt.dgraph.error.resource_not_found_error import ResourceNotFoundError

TEST_HOST = "TEST_HOST"
TEST_HOST_2 = "TEST_HOST_2"
TEST_PORT = 8080
TEST_NODE_TYPE = "TEST_NODE_TYPE"
TEST_NODE_TYPE_2 = "TEST_NODE_TYPE_2"
TEST_ATTR_NAME = "TEST_ATTR_NAME"
TEST_ATTR_NAME_2 = "TEST_ATTR_NAME_2"
TEST_ATTR_TYPE = SchemaAttributeType.STRING
TEST_ATTR_TYPE_2 = SchemaAttributeType.INT
TEST_ATTR_VALUE = "TEST_ATTR_VALUE"
TEST_ATTR_VALUE_2 = 0
TEST_IS_LIST_TYPE_TRUE = True
TEST_IS_LIST_TYPE_FALSE = False
TEST_INDICES_1 = {StringIndex.EXACT}
TEST_SCHEMA_STATEMENT = "TEST_ATTR_NAME: [string] @index(exact) .\n" + \
                        "TEST_ATTR_NAME_2: int .\n" + \
                        "type TEST_NODE_TYPE {\n" + \
                        "TEST_ATTR_NAME\n" + \
                        "}\n"+ \
                        "type TEST_NODE_TYPE_2 {\n" + \
                        "TEST_ATTR_NAME_2\n" + \
                        "}"
TEST_NODE_ID = "0x1"
TEST_EMPTY_GET_RESPONSE = '{"target":[]}'
TEST_SCALAR_TYPE = ScalarType.STRING
TEST_SCALAR_TYPE_2 = ScalarType.INT
TEST_GET_RESPONSE_1 = '{"target":[{"TEST_ATTR_NAME":["TEST_ATTR_VALUE"]}]}'
TEST_GET_RESPONSE_2 = '{"target":[{"TEST_ATTR_NAME_2":0}]}'
class DGraphClientTestCase(unittest.TestCase):

    @patch("pydgraph.DgraphClientStub")
    def test_constructor(self, mock_client_stub) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
        dgraph_client = DGraphClient(hosts=server_address_set)
        self.assertEqual(dgraph_client.hosts, server_address_set)
        mock_client_stub.assert_any_call(server_address.get_address())
        mock_client_stub.assert_any_call(server_address2.get_address())

    @patch("pydgraph.Operation")
    def test_set_schema(self, mock_operation) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
        dgraph_client = DGraphClient(hosts=server_address_set)
        dgraph_client._client.alter = MagicMock(return_value=None)

        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME_2,
                                       attr_type=TEST_ATTR_TYPE_2,
                                       is_list_type=TEST_IS_LIST_TYPE_FALSE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])
        node_schema2 = NodeSchema(TEST_NODE_TYPE_2, [type_attribute2])
        dgraph_schema = DGraphSchema([node_schema, node_schema2])

        dgraph_client.set_schema(dgraph_schema)
        mock_operation.assert_called_with(schema=TEST_SCHEMA_STATEMENT)

    def test_get_resource_successful_list_attribute(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
        dgraph_client = DGraphClient(hosts=server_address_set)

        mock_query_response = MagicMock()
        mock_query_response.json = TEST_GET_RESPONSE_1
        mock_query = MagicMock()
        mock_query.query = MagicMock(return_value=mock_query_response)
        dgraph_client._client.txn = MagicMock(return_value=mock_query)

        node_id = NodeId(TEST_NODE_ID)
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])

        expected = Node(node_id)
        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        expected.add_predicate(predicate)
        actual = dgraph_client.get(node_id, node_schema)
        self.assertEqual(expected, actual)

    def test_get_resource_successful_scalar_attribute(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
        dgraph_client = DGraphClient(hosts=server_address_set)

        mock_query_response = MagicMock()
        mock_query_response.json = TEST_GET_RESPONSE_2
        mock_query = MagicMock()
        mock_query.query = MagicMock(return_value=mock_query_response)
        dgraph_client._client.txn = MagicMock(return_value=mock_query)

        node_id = NodeId(TEST_NODE_ID)
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME_2,
                                       attr_type=TEST_ATTR_TYPE_2,
                                       is_list_type=TEST_IS_LIST_TYPE_FALSE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])

        expected = Node(node_id)
        predicate = ScalarPredicate(TEST_ATTR_NAME_2, TEST_ATTR_VALUE_2, TEST_SCALAR_TYPE_2)
        expected.add_predicate(predicate)
        actual = dgraph_client.get(node_id, node_schema)
        self.assertEqual(expected, actual)

    def test_get_resource_successful_partial(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
        dgraph_client = DGraphClient(hosts=server_address_set)

        mock_query_response = MagicMock()
        mock_query_response.json = TEST_GET_RESPONSE_1
        mock_query = MagicMock()
        mock_query.query = MagicMock(return_value=mock_query_response)
        dgraph_client._client.txn = MagicMock(return_value=mock_query)

        node_id = NodeId(TEST_NODE_ID)
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME_2,
                                       attr_type=TEST_ATTR_TYPE_2,
                                       is_list_type=TEST_IS_LIST_TYPE_FALSE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute, type_attribute2])

        expected = Node(node_id)
        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        expected.add_predicate(predicate)
        actual = dgraph_client.get(node_id, node_schema)
        self.assertEqual(expected, actual)
    

    def test_get_resource_not_found_error(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
        dgraph_client = DGraphClient(hosts=server_address_set)

        mock_query_response = MagicMock()
        mock_query_response.json = TEST_EMPTY_GET_RESPONSE
        mock_query = MagicMock()
        mock_query.query = MagicMock(return_value=mock_query_response)
        dgraph_client._client.txn = MagicMock(return_value=mock_query)

        node_id = NodeId(TEST_NODE_ID)
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])

        def get_node() -> None:
            dgraph_client.get(node_id, node_schema)

        self.assertRaises(ResourceNotFoundError, get_node)

    def test_get_internal_server_error(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
        dgraph_client = DGraphClient(hosts=server_address_set)

        
        mock_query = MagicMock()
        mock_query.query = MagicMock(side_effect=AbortedError())
        dgraph_client._client.txn = MagicMock(return_value=mock_query)

        node_id = NodeId(TEST_NODE_ID)
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])

        def get_node() -> None:
            dgraph_client.get(node_id, node_schema)

        self.assertRaises(InternalServerError, get_node)


