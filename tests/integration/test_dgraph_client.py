import unittest

from dt.dgraph.client.dgraph_client import DGraphClient
from dt.dgraph.client.server_address import ServerAddress
from dt.dgraph.constants.index_type import DateTimeIndex, StringIndex
from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.dql.dgraph_schema import DGraphSchema
from dt.dgraph.dql.node_schema import NodeSchema
from dt.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.dgraph.dql.type_attribute import TypeAttribute
from dt.dgraph.entity.node import Node
from dt.dns_trawler.error.resource_already_exists_error import \
    ResourceAlreadyExistsError
from dt.dns_trawler.error.resource_not_found_error import ResourceNotFoundError

DGRAPH_HOST = "localhost"
DGRAPH_PORT = 9080
TEST_UID_DOES_NOT_EXIST = "0xFFFFFFFFFFFFFFFF"
TEST_BLANK_NODE_ID = "TEST_BLANK_NODE_ID"


class DGraphClientIntegrationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        server_address = ServerAddress(DGRAPH_HOST, DGRAPH_PORT)
        server_address_set = {server_address}
        dgraph_schema = DGraphSchema([
            NodeSchema(
                node_type="Person",
                attr_list=[
                    TypeAttribute(attr_name="name",
                                  attr_type=SchemaAttributeType.STRING,
                                  indices={StringIndex.TERM})
                ]
            ),
            NodeSchema(
                node_type="Film",
                attr_list=[
                    TypeAttribute(attr_name="name",
                                  attr_type=SchemaAttributeType.STRING,
                                  indices={StringIndex.TERM}),
                    TypeAttribute(attr_name="release_date",
                                  attr_type=SchemaAttributeType.DATETIME,
                                  indices={DateTimeIndex.YEAR}),
                    TypeAttribute(attr_name="revenue",
                                  attr_type=SchemaAttributeType.FLOAT),
                    TypeAttribute(attr_name="running_time",
                                  attr_type=SchemaAttributeType.INT),
                    TypeAttribute(attr_name="starring",
                                  attr_type=SchemaAttributeType.UID,
                                  is_list_type=True),
                    TypeAttribute(attr_name="director",
                                  attr_type=SchemaAttributeType.UID,
                                  is_list_type=True),
                ]
            )
        ])
        self.dgraph_client = DGraphClient(hosts=server_address_set,
                                          dgraph_schema=dgraph_schema)

    def tearDown(self) -> None:
        self.dgraph_client.close()

    def test_get_node_does_not_exist(self) -> None:
        node_key = Node(TEST_UID_DOES_NOT_EXIST)

        def get_node() -> None:
            self.dgraph_client.get(node_key)
        self.assertRaises(ResourceNotFoundError, get_node)

    def test_create_and_get_node(self) -> None:
        blank_node = Node("TEST_BLANK_NODE_ID")
        blank_node.add_predicate(ScalarPredicate(predicate_name="name",
                                                 predicate_value="test",
                                                 predicate_type=ScalarType.STRING))
        blank_node.add_predicate(ScalarPredicate(predicate_name="dgraph.type",
                                                 predicate_value="test_type",
                                                 predicate_type=ScalarType.STRING))
        retrieved_node = self.dgraph_client.get(blank_node)
        print(retrieved_node)


# print(node)
