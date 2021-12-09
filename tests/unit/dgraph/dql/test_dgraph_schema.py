import unittest

from dt.dgraph.constants.index_type import StringIndex
from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.dql.dgraph_schema import DGraphSchema
from dt.dgraph.dql.node_schema import NodeSchema
from dt.dgraph.dql.type_attribute import TypeAttribute
from dt.dgraph.error.schema_duplicate_error import SchemaDuplicateError

TEST_NODE_TYPE = "TEST_NODE_TYPE"
TEST_NODE_TYPE_2 = "TEST_NODE_TYPE_2"
TEST_ATTR_NAME = "TEST_ATTR_NAME"
TEST_ATTR_NAME_2 = "TEST_ATTR_NAME_2"
TEST_ATTR_TYPE = SchemaAttributeType.STRING
TEST_ATTR_TYPE_2 = SchemaAttributeType.INT
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


class DGraphSchemaTestCase(unittest.TestCase):
    def test_constructor_no_node_schemas(self) -> None:
        dgraph_schema = DGraphSchema()
        self.assertEqual(dgraph_schema._node_schema_list, [])
        self.assertEqual(dgraph_schema._node_schema_type_set, set())

    def test_constructor_with_node_schemas(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])
        dgraph_schema = DGraphSchema([node_schema])
        self.assertEqual(dgraph_schema._node_schema_list, [node_schema])
        self.assertEqual(dgraph_schema._node_schema_type_set, {TEST_NODE_TYPE})

    def test_add_node_schema_successful(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])
        dgraph_schema = DGraphSchema()
        dgraph_schema.add_node_schema(node_schema)
        self.assertEqual(dgraph_schema._node_schema_list, [node_schema])

    def test_add_node_schema_error(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])
        dgraph_schema = DGraphSchema([node_schema])

        def add_node_schema() -> None:
            dgraph_schema.add_node_schema(node_schema)
        self.assertRaises(SchemaDuplicateError, add_node_schema)

    def test_get_attribute_dict_successful_no_duplicates(self) -> None:
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
        self.assertEqual(dgraph_schema.get_attribute_dict(), {
            TEST_ATTR_NAME: type_attribute,
            TEST_ATTR_NAME_2: type_attribute2
        })

    def test_get_attribute_dict_successful_duplicates(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])
        node_schema2 = NodeSchema(TEST_NODE_TYPE_2, [type_attribute])
        dgraph_schema = DGraphSchema([node_schema, node_schema2])
        self.assertEqual(dgraph_schema.get_attribute_dict(), {
            TEST_ATTR_NAME: type_attribute,
        })

    def test_get_attribute_dict_error(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                        attr_type=TEST_ATTR_TYPE_2,
                                        is_list_type=TEST_IS_LIST_TYPE_FALSE)
        node_schema = NodeSchema(TEST_NODE_TYPE, [type_attribute])
        node_schema2 = NodeSchema(TEST_NODE_TYPE_2, [type_attribute2])
        dgraph_schema = DGraphSchema([node_schema, node_schema2])

        def get_attribute_dict() -> None:
            dgraph_schema.get_attribute_dict()
        self.assertRaises(SchemaDuplicateError, get_attribute_dict)

    def test_get_attributes(self) -> None:
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
        self.assertEqual(dgraph_schema.get_attributes(), [type_attribute, type_attribute2])

    def test_to_schema_statement(self) -> None:
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
        self.assertEqual(dgraph_schema.to_schema_statement(), TEST_SCHEMA_STATEMENT)
