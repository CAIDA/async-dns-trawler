import unittest

from dt.dgraph.graphql.variable import Variable
from dt.dgraph.graphql.variable_set import VariableSet

TEST_VARIABLE_NAME = "TEST_VARIABLE_NAME"
TEST_VARIABLE_TYPE = "string"
TEST_VARIABLE_NAME_2 = "TEST_VARIABLE_NAME_2"
TEST_GRAPHQL_STR = "$TEST_VARIABLE_NAME: string, $TEST_VARIABLE_NAME_2: string"


class VariableSetTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        variable = Variable(TEST_VARIABLE_NAME, TEST_VARIABLE_TYPE)
        variable_set = VariableSet(variable)
        expected = {variable}
        actual = variable_set.items
        self.assertEqual(actual, expected)

    def test_eq_equal(self) -> None:
        variable = Variable(TEST_VARIABLE_NAME, TEST_VARIABLE_TYPE)
        variable_set = VariableSet(variable)
        variable_set2 = VariableSet(variable)
        self.assertEqual(variable_set, variable_set2)

    def test_eq_not_equal(self) -> None:
        variable = Variable(TEST_VARIABLE_NAME, TEST_VARIABLE_TYPE)
        variable2 = Variable(TEST_VARIABLE_NAME_2, TEST_VARIABLE_TYPE)
        variable_set = VariableSet(variable)
        variable_set2 = VariableSet(variable2)
        self.assertNotEqual(variable_set, variable_set2)

    def test_eq_not_equal_different_class(self) -> None:
        variable = Variable(TEST_VARIABLE_NAME, TEST_VARIABLE_TYPE)
        variable_set = VariableSet(variable)
        variable_set2 = object()
        self.assertNotEqual(variable_set, variable_set2)

    def test_hash_equal(self) -> None:
        variable = Variable(TEST_VARIABLE_NAME, TEST_VARIABLE_TYPE)
        variable_set = VariableSet(variable)
        variable_set2 = VariableSet(variable)
        self.assertEqual(hash(variable_set), hash(variable_set2))

    def test_hash_not_equal(self) -> None:
        variable = Variable(TEST_VARIABLE_NAME, TEST_VARIABLE_TYPE)
        variable2 = Variable(TEST_VARIABLE_NAME_2, TEST_VARIABLE_TYPE)
        variable_set = VariableSet(variable)
        variable_set2 = VariableSet(variable2)
        self.assertNotEqual(hash(variable_set), hash(variable_set2))

    def test_to_graphql(self) -> None:
        variable = Variable(TEST_VARIABLE_NAME, TEST_VARIABLE_TYPE)
        variable2 = Variable(TEST_VARIABLE_NAME_2, TEST_VARIABLE_TYPE)
        variable_set = VariableSet(variable, variable2)
        expected = TEST_GRAPHQL_STR
        actual = variable_set.to_graphql()
        self.assertEqual(actual, expected)
