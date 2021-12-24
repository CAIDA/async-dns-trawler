import unittest

from dt.client.dgraph.constants.schema_attribute_type import \
    SchemaAttributeType
from dt.client.dgraph.dql.node_schema import NodeSchema
from dt.client.dgraph.dql.type_attribute import TypeAttribute
from dt.client.dgraph.error.schema_duplicate_error import SchemaDuplicateError

TEST_NODE_TYPE = "TEST_NODE_TYPE"
TEST_ATTR_NAME = "TEST_ATTR_NAME"
TEST_ATTR_TYPE = SchemaAttributeType.STRING
TEST_IS_LIST_TYPE_TRUE = True
TEST_SCHEMA_STATEMENT = "type TEST_NODE_TYPE {\n" + \
                        "TEST_ATTR_NAME\n" + \
                        "}"


class NodeSchemaTestCase(unittest.TestCase):
    def test_constructor_no_attributes(self) -> None:
        node_schema = NodeSchema(TEST_NODE_TYPE)
        self.assertEqual(node_schema.node_type, TEST_NODE_TYPE)
        self.assertEqual(node_schema._attribute_list, [])
        self.assertEqual(node_schema._attribute_name_set, set())

    def test_constructor_with_attributes(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])
        self.assertEqual(node_schema.node_type, TEST_NODE_TYPE)
        self.assertEqual(node_schema._attribute_list, [type_attribute])
        self.assertEqual(node_schema._attribute_name_set, {TEST_ATTR_NAME})

    def test_add_attribute_successful(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        node_schema = NodeSchema(TEST_NODE_TYPE)
        node_schema.add_attribute(type_attribute)
        self.assertEqual(node_schema._attribute_list, [type_attribute])

    def test_add_attribute_error(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])

        def add_attribute() -> None:
            node_schema.add_attribute(type_attribute)
        self.assertRaises(SchemaDuplicateError, add_attribute)

    def test_get_attributes(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        node_schema = NodeSchema(TEST_NODE_TYPE)
        node_schema.add_attribute(type_attribute)
        self.assertEqual(node_schema.get_attributes(), [type_attribute])

    def test_to_schema_statement(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])
        self.assertEqual(node_schema.to_schema_statement(), TEST_SCHEMA_STATEMENT)
