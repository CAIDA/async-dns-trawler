import unittest
from enum import Enum

from dt.dgraph.graphql.value import Value

TEST_INT_VALUE = 5
TEST_INT_VALUE_GRAPHQL_STR = "5"
TEST_STR_VALUE = "TEST_STR_VALUE"
TEST_STR_VALUE_GRAPHQL_STR = "TEST_STR_VALUE"
TEST_ENUM_VALUE_GRAPHQL_STR = "test_value"


class TestEnum(Enum):
    TEST_VALUE = "test_value"


class ValueTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        value = Value(TEST_STR_VALUE)
        self.assertEqual(value.value, TEST_STR_VALUE)

    def test_eq_equal(self) -> None:
        value = Value(TEST_STR_VALUE)
        value2 = Value(TEST_STR_VALUE)
        self.assertEqual(value, value2)

    def test_eq_not_equal(self) -> None:
        value = Value(TEST_STR_VALUE)
        value2 = Value(TEST_INT_VALUE)
        self.assertNotEqual(value, value2)

    def test_eq_not_equal_different_class(self) -> None:
        value = Value(TEST_STR_VALUE)
        value2 = object()
        self.assertNotEqual(value, value2)

    def test_hash_equal(self) -> None:
        value = Value(TEST_STR_VALUE)
        value2 = Value(TEST_STR_VALUE)
        self.assertEqual(hash(value), hash(value2))

    def test_hash_not_equal(self) -> None:
        value = Value(TEST_STR_VALUE)
        value2 = Value(TEST_INT_VALUE)
        self.assertNotEqual(hash(value), hash(value2))

    def test_to_graphql_int(self) -> None:
        value = Value(TEST_INT_VALUE)
        expected = TEST_INT_VALUE_GRAPHQL_STR
        actual = value.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_str(self) -> None:
        value = Value(TEST_STR_VALUE)
        expected = TEST_STR_VALUE_GRAPHQL_STR
        actual = value.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_enum(self) -> None:
        value = Value(TestEnum.TEST_VALUE)
        expected = TEST_ENUM_VALUE_GRAPHQL_STR
        actual = value.to_graphql()
        self.assertEqual(actual, expected)
