import unittest

from dt.client.dgraph.graphql.value import Value
from dt.client.dgraph.graphql.variable import Variable
from dt.client.dgraph.graphql.variable_reference import VariableReference

TEST_NAME = "TEST_NAME"
TEST_NAME_2 = "TEST_NAME_2"
TEST_VARIABLE_TYPE = "TEST_VARIABLE_TYPE"
TEST_VARIABLE_TYPE_2 = "TEST_VARIABLE_TYPE_2"
TEST_VALUE = "TEST_VALUE"
TEST_VALUE_2 = "TEST_VALUE_2"
TEST_DEFAULT_VALUE = "TEST_DEFAULT_VALUE"
TEST_DEFAULT_VALUE_2 = "TEST_DEFAULT_VALUE_2"
TEST_GRAPHQL_STR = "$TEST_NAME: TEST_VARIABLE_TYPE"
TEST_GRAPHQL_STR_WITH_DEFAULT_VALUE = \
    "$TEST_NAME: TEST_VARIABLE_TYPE = TEST_DEFAULT_VALUE"


class VariableTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        self.assertEqual(variable.name, TEST_NAME)
        self.assertEqual(variable.variable_type, TEST_VARIABLE_TYPE)
        self.assertEqual(variable.value, value)
        self.assertEqual(variable.default_value, default_value)

    def test_get_reference(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        expected = VariableReference(TEST_NAME)
        actual = variable.get_reference()
        self.assertEqual(actual, expected)

    def test_eq_equal(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        variable2 = Variable(name=TEST_NAME,
                             variable_type=TEST_VARIABLE_TYPE,
                             value=value,
                             default_value=default_value)
        self.assertEqual(variable, variable2)

    def test_eq_not_equal_different_name(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        variable2 = Variable(name=TEST_NAME_2,
                             variable_type=TEST_VARIABLE_TYPE,
                             value=value,
                             default_value=default_value)
        self.assertNotEqual(variable, variable2)

    def test_eq_not_equal_different_variable_type(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        variable2 = Variable(name=TEST_NAME,
                             variable_type=TEST_VARIABLE_TYPE_2,
                             value=value,
                             default_value=default_value)
        self.assertNotEqual(variable, variable2)

    def test_eq_not_equal_different_value(self) -> None:
        value = Value(TEST_VALUE)
        value2 = Value(TEST_VALUE_2)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        variable2 = Variable(name=TEST_NAME,
                             variable_type=TEST_VARIABLE_TYPE,
                             value=value2,
                             default_value=default_value)
        self.assertNotEqual(variable, variable2)

    def test_eq_not_equal_different_default_value(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        default_value_2 = Value(TEST_DEFAULT_VALUE_2)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        variable2 = Variable(name=TEST_NAME,
                             variable_type=TEST_VARIABLE_TYPE,
                             value=value,
                             default_value=default_value_2)
        self.assertNotEqual(variable, variable2)

    def test_eq_not_equal_different_class(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        variable2 = object()
        self.assertNotEqual(variable, variable2)

    def test_hash_equal(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        variable2 = Variable(name=TEST_NAME,
                             variable_type=TEST_VARIABLE_TYPE,
                             value=value,
                             default_value=default_value)
        self.assertEqual(hash(variable), hash(variable2))

    def test_hash_not_equal(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        variable2 = Variable(name=TEST_NAME_2,
                             variable_type=TEST_VARIABLE_TYPE_2,
                             value=value,
                             default_value=default_value)
        self.assertNotEqual(hash(variable), hash(variable2))

    def test_to_graphql(self) -> None:
        value = Value(TEST_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value)
        expected = TEST_GRAPHQL_STR
        actual = variable.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_with_default_value(self) -> None:
        value = Value(TEST_VALUE)
        default_value = Value(TEST_DEFAULT_VALUE)
        variable = Variable(name=TEST_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=value,
                            default_value=default_value)
        expected = TEST_GRAPHQL_STR_WITH_DEFAULT_VALUE
        actual = variable.to_graphql()
        self.assertEqual(actual, expected)
