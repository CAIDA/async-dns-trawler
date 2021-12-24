import unittest

from dt.client.dgraph.constants.comparison_function import ComparisonFunction
from dt.client.dgraph.dql.query_function import QueryFunction
from dt.client.dgraph.graphql.value import Value

TEST_ARG_1 = "TEST_ARG_1"
TEST_ARG_2 = "TEST_ARG_2"
TEST_COMPARISON_FUNCTION = ComparisonFunction.EQ
TEST_COMPARISON_FUNCTION_2 = ComparisonFunction.LE
TEST_GRAPHQL_STR = "eq(TEST_ARG_1, TEST_ARG_2)"


class QueryFunctionTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        self.assertEqual(query_function.comp_func, TEST_COMPARISON_FUNCTION)
        self.assertEqual(query_function.args, args)

    def test_eq_equal(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_function2 = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        self.assertEqual(query_function, query_function2)

    def test_eq_not_equal_different_comparision_function(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_function2 = QueryFunction(TEST_COMPARISON_FUNCTION_2, args)
        self.assertNotEqual(query_function, query_function2)

    def test_eq_not_equal_different_args(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        args2 = (Value(TEST_ARG_1),)
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_function2 = QueryFunction(TEST_COMPARISON_FUNCTION, args2)
        self.assertNotEqual(query_function, query_function2)

    def test_eq_not_equal_different_class(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_function2 = object()
        self.assertNotEqual(query_function, query_function2)

    def test_hash_equal(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function2 = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        self.assertEqual(hash(query_function), hash(query_function2))

    def test_hash_not_equal(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_function2 = QueryFunction(TEST_COMPARISON_FUNCTION_2, args)
        self.assertNotEqual(hash(query_function), hash(query_function2))

    def test_to_graphql_int(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        expected = TEST_GRAPHQL_STR
        actual = query_function.to_graphql()
        self.assertEqual(actual, expected)
