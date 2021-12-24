import unittest

from dt.client.dgraph.graphql.variable_reference import VariableReference

TEST_VARIABLE_NAME = "TEST_VARIABLE_NAME"
TEST_VARIABLE_NAME_2 = "TEST_VARIABLE_NAME_2"
TEST_GRAPHQL_STR = "$TEST_VARIABLE_NAME"


class VariableReferenceTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        var_ref = VariableReference(TEST_VARIABLE_NAME)
        self.assertEqual(var_ref.variable_name, TEST_VARIABLE_NAME)

    def test_eq_equal(self) -> None:
        var_ref = VariableReference(TEST_VARIABLE_NAME)
        var_ref2 = VariableReference(TEST_VARIABLE_NAME)
        self.assertEqual(var_ref, var_ref2)

    def test_eq_not_equal(self) -> None:
        var_ref = VariableReference(TEST_VARIABLE_NAME)
        var_ref2 = VariableReference(TEST_VARIABLE_NAME_2)
        self.assertNotEqual(var_ref, var_ref2)

    def test_eq_not_equal_different_class(self) -> None:
        var_ref = VariableReference(TEST_VARIABLE_NAME)
        var_ref2 = object()
        self.assertNotEqual(var_ref, var_ref2)

    def test_hash_equal(self) -> None:
        var_ref = VariableReference(TEST_VARIABLE_NAME)
        var_ref2 = VariableReference(TEST_VARIABLE_NAME)
        self.assertEqual(hash(var_ref), hash(var_ref2))

    def test_hash_not_equal(self) -> None:
        var_ref = VariableReference(TEST_VARIABLE_NAME)
        var_ref2 = VariableReference(TEST_VARIABLE_NAME_2)
        self.assertNotEqual(hash(var_ref), hash(var_ref2))

    def test_to_graphql_int(self) -> None:
        var_ref = VariableReference(TEST_VARIABLE_NAME)
        expected = TEST_GRAPHQL_STR
        actual = var_ref.to_graphql()
        self.assertEqual(actual, expected)
