import typing
import unittest
from typing import Any
from unittest.mock import Mock, patch

from pydgraph.errors import AbortedError

from dt.client.dgraph.client.dgraph_client import DGraphClient
from dt.client.dgraph.client.server_address import ServerAddress
from dt.client.dgraph.constants.index_type import StringIndex
from dt.client.dgraph.constants.mutation_type import MutationType
from dt.client.dgraph.constants.scalar_type import ScalarType
from dt.client.dgraph.constants.schema_attribute_type import \
    SchemaAttributeType
from dt.client.dgraph.dql.dgraph_schema import DGraphSchema
from dt.client.dgraph.dql.node_schema import NodeSchema
from dt.client.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.client.dgraph.dql.type_attribute import TypeAttribute
from dt.client.dgraph.entity.blank_node import BlankNode
from dt.client.dgraph.entity.node import Node
from dt.client.dgraph.error.mutation_error import MutationError
from dt.dns_trawler.constants.sort_direction import SortDirection
from dt.dns_trawler.db.order_by import OrderBy
from dt.dns_trawler.db.query_field import QueryField
from dt.dns_trawler.db.query_options import QueryOptions
from dt.dns_trawler.db.query_response import QueryResponse
from dt.dns_trawler.error.internal_server_error import InternalServerError
from dt.dns_trawler.error.resource_already_exists_error import \
    ResourceAlreadyExistsError
from dt.dns_trawler.error.resource_not_found_error import ResourceNotFoundError
from dt.dns_trawler.error.validation_error import ValidationError
from tests.util.dgraph_client_mocker import DGraphClientMocker

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
                        "}\n" + \
                        "type TEST_NODE_TYPE_2 {\n" + \
                        "TEST_ATTR_NAME_2\n" + \
                        "}"
TEST_NODE_ID = "0x1"
TEST_NODE_ID_2 = "0x2"
TEST_BLANK_NODE_ID = "TEST_BLANK_NODE_ID"
TEST_EMPTY_GET_RESPONSE = '{"get":[]}'
TEST_SCALAR_TYPE = ScalarType.STRING
TEST_SCALAR_TYPE_2 = ScalarType.INT
TEST_MAX_RESULTS = 1
TEST_GET_RESPONSE_1 = '{"get":[{"uid":"0x1", "TEST_ATTR_NAME":["TEST_ATTR_VALUE"]}]}'
TEST_GET_RESPONSE_2 = '{"get":[{"uid":"0x1", "TEST_ATTR_NAME_2":0}]}'
TEST_GET_RESPONSE_3 = '{"get":[{"uid":"0x1", "TEST_ATTR_NAME":["TEST_ATTR_VALUE"], "TEST_ATTR_NAME_2":0}]}'
TEST_QUERY_RESPONSE_1 = '{"get":[{"uid":"0x1", "TEST_ATTR_NAME_2":0},{"uid":"0x2", "TEST_ATTR_NAME_2":0}]}'
TEST_QUERY_RESPONSE_2 = '{"get":[{"uid":"0x1", "TEST_ATTR_NAME_2":0}]}'
TEST_QUERY_RESPONSE_3 = '{"get":[{"uid":"0x2", "TEST_ATTR_NAME_2":0}]}'
TEST_QUERY_RESPONSE_4 = '{"get":[{"uid":"0x2", "TEST_ATTR_NAME_2":0},{"uid":"0x1", "TEST_ATTR_NAME_2":0}]}'
TEST_EMPTY_QUERY_RESPONSE = '{"get":[]}'
TEST_INVALID_QUERY_RESPONSE = '{"get":[{"TEST_ATTR_NAME_2":0},{"uid":"0x1", "TEST_ATTR_NAME_2":0}]}'
TEST_INVALID_QUERY_RESPONSE_2 = '{"get":[{"TEST_ATTR_NAME_3":0, "uid":"0x2"},{"uid":"0x1", "TEST_ATTR_NAME_2":0}]}'


class DGraphClientTestCase(unittest.TestCase):
    def setUp(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
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
        self.dgraph_client = DGraphClient(hosts=server_address_set,
                                          dgraph_schema=dgraph_schema)

    def tearDown(self) -> None:
        self.dgraph_client.close()

    @patch("pydgraph.DgraphClientStub")
    def test_constructor(self, mock_client_stub: Mock) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        server_address_set = {server_address, server_address2}
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
        dgraph_client = DGraphClient(hosts=server_address_set,
                                     dgraph_schema=dgraph_schema)
        self.assertEqual(dgraph_client.hosts, server_address_set)
        self.assertEqual(dgraph_client.dgraph_schema, dgraph_schema)
        mock_client_stub.assert_any_call(server_address.get_address())
        mock_client_stub.assert_any_call(server_address2.get_address())

    @patch("pydgraph.Operation")
    def test_set_schema(self, mock_operation: Mock) -> None:
        DGraphClientMocker.mock_alter(self.dgraph_client._client)

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

        self.dgraph_client.set_schema(dgraph_schema)
        mock_operation.assert_called_with(schema=TEST_SCHEMA_STATEMENT)
        self.assertEqual(self.dgraph_client.dgraph_schema, dgraph_schema)

    def test_get_resource_successful_list_attribute(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})

        expected = Node(TEST_NODE_ID)
        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        expected.add_predicate(predicate)
        actual = self.dgraph_client.get(Node(TEST_NODE_ID))
        self.assertEqual(expected, actual)

    def test_get_resource_successful_scalar_attribute(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_2})

        expected = Node(TEST_NODE_ID)
        predicate = ScalarPredicate(TEST_ATTR_NAME_2, TEST_ATTR_VALUE_2, TEST_SCALAR_TYPE_2)
        expected.add_predicate(predicate)
        actual = self.dgraph_client.get(Node(TEST_NODE_ID))
        self.assertEqual(expected, actual)

    def test_get_resource_successful_partial(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})

        expected = Node(TEST_NODE_ID)
        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        expected.add_predicate(predicate)
        actual = self.dgraph_client.get(Node(TEST_NODE_ID))
        self.assertEqual(expected, actual)

    def test_get_resource_not_found_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_GET_RESPONSE})

        def get_node() -> None:
            self.dgraph_client.get(Node(TEST_NODE_ID))

        self.assertRaises(ResourceNotFoundError, get_node)

    def test_get_internal_server_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, triggers=AbortedError())

        def get_node() -> None:
            self.dgraph_client.get(Node(TEST_NODE_ID))

        self.assertRaises(InternalServerError, get_node)

    def test_create_successful_blank_node(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_GET_RESPONSE})

        def update_query_response(*args: Any, **kwargs: Any) -> unittest.mock.DEFAULT:
            DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})
            return unittest.mock.DEFAULT
        DGraphClientMocker.mock_mutate(
            self.dgraph_client._client,
            returns={
                'uids': {
                    TEST_BLANK_NODE_ID: TEST_NODE_ID}},
            triggers=update_query_response)

        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        expected = Node(TEST_NODE_ID)
        expected.add_predicate(predicate)

        blank_node = BlankNode(TEST_BLANK_NODE_ID)
        blank_node.add_predicate(predicate)

        actual = self.dgraph_client.create(blank_node)
        self.assertEqual(actual, expected)

    def test_create_successful_node(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_GET_RESPONSE})

        def update_query_response(*args: Any, **kwargs: Any) -> unittest.mock.DEFAULT:
            DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})
            return unittest.mock.DEFAULT
        DGraphClientMocker.mock_mutate(self.dgraph_client._client, triggers=update_query_response)

        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        expected = Node(TEST_NODE_ID)
        expected.add_predicate(predicate)

        node = Node(TEST_NODE_ID)
        node.add_predicate(predicate)

        actual = self.dgraph_client.create(node)
        self.assertEqual(actual, expected)

    def test_create_resource_already_exists_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})

        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        blank_node = BlankNode(TEST_BLANK_NODE_ID)
        blank_node.add_predicate(predicate)

        def create() -> None:
            self.dgraph_client.create(blank_node)
        self.assertRaises(ResourceAlreadyExistsError, create)

    def test_create_validation_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_GET_RESPONSE})

        def update_query_response(*args: Any, **kwargs: Any) -> unittest.mock.DEFAULT:
            DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})
            return unittest.mock.DEFAULT
        DGraphClientMocker.mock_mutate(self.dgraph_client._client, returns={'uids': {}}, triggers=update_query_response)

        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        blank_node = BlankNode(TEST_BLANK_NODE_ID)
        blank_node.add_predicate(predicate)

        def create() -> None:
            self.dgraph_client.create(blank_node)
        self.assertRaises(ValidationError, create)

    def test_create_internal_server_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_GET_RESPONSE})
        DGraphClientMocker.mock_mutate(self.dgraph_client._client, triggers=AbortedError())

        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        blank_node = BlankNode(TEST_BLANK_NODE_ID)
        blank_node.add_predicate(predicate)

        def create() -> None:
            self.dgraph_client.create(blank_node)
        self.assertRaises(InternalServerError, create)

    def test_update_successful(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})

        def update_query_response(*args: Any, **kwargs: Any) -> unittest.mock.DEFAULT:
            DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_3})
            return unittest.mock.DEFAULT
        DGraphClientMocker.mock_mutate(self.dgraph_client._client, triggers=update_query_response)

        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        predicate2 = ScalarPredicate(TEST_ATTR_NAME_2, TEST_ATTR_VALUE_2, TEST_SCALAR_TYPE_2)
        expected = Node(TEST_NODE_ID)
        expected.add_predicate(predicate)
        expected.add_predicate(predicate2)

        node = Node(TEST_NODE_ID)
        node.add_predicate(predicate)
        node.add_predicate(predicate2)

        actual = self.dgraph_client.update(node)
        self.assertEqual(actual, expected)

    def test_update_resource_not_found_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_GET_RESPONSE})

        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        node = Node(TEST_NODE_ID)
        node.add_predicate(predicate)

        def update() -> None:
            self.dgraph_client.update(node)
        self.assertRaises(ResourceNotFoundError, update)

    def test_update_internal_server_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})
        DGraphClientMocker.mock_mutate(self.dgraph_client._client, triggers=AbortedError())

        predicate = ScalarPredicate(TEST_ATTR_NAME, TEST_ATTR_VALUE, TEST_SCALAR_TYPE)
        node = Node(TEST_NODE_ID)
        node.add_predicate(predicate)

        def update() -> None:
            self.dgraph_client.update(node)
        self.assertRaises(InternalServerError, update)

    def test_delete_successful(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})

        def update_query_response(*args: Any, **kwargs: Any) -> unittest.mock.DEFAULT:
            DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_GET_RESPONSE})
            return unittest.mock.DEFAULT

        node = Node(TEST_NODE_ID)
        try:
            self.dgraph_client.delete(node)
        except BaseException:
            self.fail()

    def test_delete_successful_noop(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_GET_RESPONSE})

        node = Node(TEST_NODE_ID)
        try:
            self.dgraph_client.delete(node)
        except BaseException:
            self.fail()

    def test_delete_internal_server_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_GET_RESPONSE_1})
        DGraphClientMocker.mock_mutate(self.dgraph_client._client, triggers=AbortedError())

        node = Node(TEST_NODE_ID)

        def delete() -> None:
            self.dgraph_client.delete(node)
        self.assertRaises(InternalServerError, delete)

    def test_query_successful(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_QUERY_RESPONSE_1})
        node = Node(TEST_NODE_ID)
        node2 = Node(TEST_NODE_ID_2)
        predicate = ScalarPredicate(TEST_ATTR_NAME_2, TEST_ATTR_VALUE_2, TEST_SCALAR_TYPE_2)
        node.add_predicate(predicate)
        node2.add_predicate(predicate)
        expected = QueryResponse[Node](items=[node, node2])
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(0)
        query_options = QueryOptions(expression=expression)
        actual = self.dgraph_client.query(query_options)
        self.assertEqual(actual, expected)

    def test_query_successful_with_max_results(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_QUERY_RESPONSE_2})
        node = Node(TEST_NODE_ID)
        predicate = ScalarPredicate(TEST_ATTR_NAME_2, TEST_ATTR_VALUE_2, TEST_SCALAR_TYPE_2)
        node.add_predicate(predicate)
        expected = QueryResponse[Node](items=[node], next_token=TEST_NODE_ID)
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(0)
        query_options = QueryOptions(expression=expression, max_results=TEST_MAX_RESULTS)
        actual = self.dgraph_client.query(query_options)
        self.assertEqual(actual, expected)

    def test_query_successful_with_next_token(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_QUERY_RESPONSE_3})
        node = Node(TEST_NODE_ID_2)
        predicate = ScalarPredicate(TEST_ATTR_NAME_2, TEST_ATTR_VALUE_2, TEST_SCALAR_TYPE_2)
        node.add_predicate(predicate)
        expected = QueryResponse[Node](items=[node])
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(0)
        query_options = QueryOptions(expression=expression, next_token=TEST_NODE_ID)
        actual = self.dgraph_client.query(query_options)
        self.assertEqual(actual, expected)

    def test_query_successful_with_order_by_asc(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_QUERY_RESPONSE_1})
        node = Node(TEST_NODE_ID)
        node2 = Node(TEST_NODE_ID_2)
        predicate = ScalarPredicate(TEST_ATTR_NAME_2, TEST_ATTR_VALUE_2, TEST_SCALAR_TYPE_2)
        node.add_predicate(predicate)
        node2.add_predicate(predicate)
        expected = QueryResponse[Node](items=[node, node2])
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(0)
        order_by = OrderBy(QueryField('uid'), SortDirection.ASC)
        query_options = QueryOptions(expression=expression, order_by=order_by)
        actual = self.dgraph_client.query(query_options)
        self.assertEqual(actual, expected)

    def test_query_successful_with_order_by_desc(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_QUERY_RESPONSE_4})
        node = Node(TEST_NODE_ID)
        node2 = Node(TEST_NODE_ID_2)
        predicate = ScalarPredicate(TEST_ATTR_NAME_2, TEST_ATTR_VALUE_2, TEST_SCALAR_TYPE_2)
        node.add_predicate(predicate)
        node2.add_predicate(predicate)
        expected = QueryResponse[Node](items=[node2, node])
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(0)
        order_by = OrderBy(QueryField('uid'), SortDirection.DESC)
        query_options = QueryOptions(expression=expression, order_by=order_by)
        actual = self.dgraph_client.query(query_options)
        self.assertEqual(actual, expected)

    def test_query_successful_empty_response(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_QUERY_RESPONSE})
        expected = QueryResponse[Node](items=[])
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(1)
        query_options = QueryOptions(expression=expression)
        actual = self.dgraph_client.query(query_options)
        self.assertEqual(actual, expected)

    def test_query_successful_empty_response_with_max_results(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_EMPTY_QUERY_RESPONSE})
        expected = QueryResponse[Node](items=[])
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(1)
        query_options = QueryOptions(expression=expression, max_results=TEST_MAX_RESULTS)
        actual = self.dgraph_client.query(query_options)
        self.assertEqual(actual, expected)

    def test_query_validation_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_INVALID_QUERY_RESPONSE})
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(1)
        query_options = QueryOptions(expression=expression)

        def query() -> None:
            self.dgraph_client.query(query_options)
        self.assertRaises(ValidationError, query)

    def test_query_resource_not_found_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, returns={'json': TEST_INVALID_QUERY_RESPONSE_2})
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(1)
        query_options = QueryOptions(expression=expression)

        def query() -> None:
            self.dgraph_client.query(query_options)
        self.assertRaises(ResourceNotFoundError, query)

    def test_query_internal_server_error(self) -> None:
        DGraphClientMocker.mock_query(self.dgraph_client._client, triggers=AbortedError())
        query_field = QueryField(TEST_ATTR_NAME_2)
        expression = query_field.eq(1)
        query_options = QueryOptions(expression=expression)

        def query() -> None:
            self.dgraph_client.query(query_options)
        self.assertRaises(InternalServerError, query)

    def test_mutate_mutation_error_mutation_type(self) -> None:
        invalid_mutation_type = typing.cast(MutationType, object())
        node = Node(TEST_NODE_ID)

        def _mutate() -> None:
            self.dgraph_client._mutate(node, invalid_mutation_type)
        self.assertRaises(MutationError, _mutate)
