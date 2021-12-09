import unittest

from dt.dgraph.constants.index_type import StringIndex
from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.dql.type_attribute import TypeAttribute

TEST_ATTR_NAME = "TEST_ATTR_NAME"
TEST_ATTR_NAME_2 = "TEST_ATTR_NAME_2"
TEST_ATTR_TYPE = SchemaAttributeType.STRING
TEST_ATTR_TYPE_2 = SchemaAttributeType.INT
TEST_IS_LIST_TYPE_TRUE = True
TEST_IS_LIST_TYPE_FALSE = False
TEST_INDICES_1 = {StringIndex.EXACT}
TEST_INDICES_2 = {StringIndex.EXACT, StringIndex.TRIGRAM}
TEST_SCHEMA_STATEMENT_1 = "TEST_ATTR_NAME: string ."
TEST_SCHEMA_STATEMENT_2 = "TEST_ATTR_NAME: [string] ."
TEST_SCHEMA_STATEMENT_3 = "TEST_ATTR_NAME: string @index(exact) ."
TEST_SCHEMA_STATEMENT_4 = "TEST_ATTR_NAME: string @index(exact, trigram) ."


class TypeAttributeTestCase(unittest.TestCase):
    def test_constructor_no_indices(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        self.assertEqual(type_attribute.attr_name, TEST_ATTR_NAME)
        self.assertEqual(type_attribute.attr_type, TEST_ATTR_TYPE)
        self.assertEqual(type_attribute.is_list_type, TEST_IS_LIST_TYPE_TRUE)
        self.assertEqual(type_attribute.indices, set())

    def test_constructor_with_indices(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        self.assertEqual(type_attribute.attr_name, TEST_ATTR_NAME)
        self.assertEqual(type_attribute.attr_type, TEST_ATTR_TYPE)
        self.assertEqual(type_attribute.is_list_type, TEST_IS_LIST_TYPE_TRUE)
        self.assertEqual(type_attribute.indices, TEST_INDICES_1)

    def test_eq_equal(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                        attr_type=TEST_ATTR_TYPE,
                                        is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                        indices=TEST_INDICES_1)
        self.assertEqual(type_attribute, type_attribute2)

    def test_eq_not_equal_attr_name(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME_2,
                                        attr_type=TEST_ATTR_TYPE,
                                        is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                        indices=TEST_INDICES_1)
        self.assertNotEqual(type_attribute, type_attribute2)

    def test_eq_not_equal_attr_type(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                        attr_type=TEST_ATTR_TYPE_2,
                                        is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                        indices=TEST_INDICES_1)
        self.assertNotEqual(type_attribute, type_attribute2)

    def test_eq_not_equal_is_list_type(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                        attr_type=TEST_ATTR_TYPE,
                                        is_list_type=TEST_IS_LIST_TYPE_FALSE,
                                        indices=TEST_INDICES_1)
        self.assertNotEqual(type_attribute, type_attribute2)

    def test_eq_not_equal_indices(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                        attr_type=TEST_ATTR_TYPE,
                                        is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                        indices=TEST_INDICES_2)
        self.assertNotEqual(type_attribute, type_attribute2)

    def test_eq_not_equal_different_class(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = object()
        self.assertNotEqual(type_attribute, type_attribute2)

    def test_lt_successful(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = TypeAttribute(attr_name=TEST_ATTR_NAME_2,
                                        attr_type=TEST_ATTR_TYPE,
                                        is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                        indices=TEST_INDICES_1)
        self.assertLess(type_attribute, type_attribute2)

    def test_lt_not_implemented(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE,
                                       indices=TEST_INDICES_1)
        type_attribute2 = object()

        def less_than() -> bool:
            return type_attribute < type_attribute2
        self.assertRaises(TypeError, less_than)

    def test_to_schema_statement_not_list_type_no_indices(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_FALSE)
        self.assertEqual(type_attribute.to_schema_statement(), TEST_SCHEMA_STATEMENT_1)

    def test_to_schema_statement_list_type(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_TRUE)
        self.assertEqual(type_attribute.to_schema_statement(), TEST_SCHEMA_STATEMENT_2)

    def test_to_schema_statement_single_index(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_FALSE,
                                       indices=TEST_INDICES_1)
        self.assertEqual(type_attribute.to_schema_statement(), TEST_SCHEMA_STATEMENT_3)

    def test_to_schema_statement_indices(self) -> None:
        type_attribute = TypeAttribute(attr_name=TEST_ATTR_NAME,
                                       attr_type=TEST_ATTR_TYPE,
                                       is_list_type=TEST_IS_LIST_TYPE_FALSE,
                                       indices=TEST_INDICES_2)
        self.assertEqual(type_attribute.to_schema_statement(), TEST_SCHEMA_STATEMENT_4)
