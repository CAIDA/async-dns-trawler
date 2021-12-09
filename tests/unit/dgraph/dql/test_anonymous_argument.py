import unittest

from dt.dgraph.dql.anonymous_argument import AnonymousArgument
from dt.dgraph.graphql.value import Value
from dt.dgraph.graphql.variable_reference import VariableReference

TEST_VALUE = "TEST_VALUE"
TEST_VALUE_2 = "TEST_VALUE_2"
TEST_VARIABLE_NAME = "TEST_VARIABLE_NAME"
TEST_GRAPHQL_STR_VALUE = "TEST_VALUE"
TEST_GRAPHQL_STR_VARIABLE = "$TEST_VARIABLE_NAME"


class AnonymousArgumentTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        input_value = Value(TEST_VALUE)
        argument = AnonymousArgument(input_value)
        self.assertEqual(argument.input_value, input_value)

    def test_eq_equal(self) -> None:
        input_value = Value(TEST_VALUE)
        argument = AnonymousArgument(input_value)
        argument2 = AnonymousArgument(input_value)
        self.assertEqual(argument, argument2)

    def test_eq_not_equal(self) -> None:
        input_value = Value(TEST_VALUE)
        input_value2 = Value(TEST_VALUE_2)
        argument = AnonymousArgument(input_value)
        argument2 = AnonymousArgument(input_value2)
        self.assertNotEqual(argument, argument2)

    def test_eq_not_equal_different_class(self) -> None:
        input_value = Value(TEST_VALUE)
        argument = AnonymousArgument(input_value)
        argument2 = object()
        self.assertNotEqual(argument, argument2)

    def test_hash_equal(self) -> None:
        input_value = Value(TEST_VALUE)
        argument = AnonymousArgument(input_value)
        argument2 = AnonymousArgument(input_value)
        self.assertEqual(hash(argument), hash(argument2))

    def test_hash_not_equal(self) -> None:
        input_value = Value(TEST_VALUE)
        input_value2 = Value(TEST_VALUE_2)
        argument = AnonymousArgument(input_value)
        argument2 = AnonymousArgument(input_value2)
        self.assertNotEqual(hash(argument), hash(argument2))

    def test_to_graphql_value(self) -> None:
        input_value = Value(TEST_VALUE)
        argument = AnonymousArgument(input_value)
        expected = TEST_GRAPHQL_STR_VALUE
        actual = argument.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_str(self) -> None:
        input_value = VariableReference(TEST_VARIABLE_NAME)
        argument = AnonymousArgument(input_value)
        expected = TEST_GRAPHQL_STR_VARIABLE
        actual = argument.to_graphql()
        self.assertEqual(actual, expected)
