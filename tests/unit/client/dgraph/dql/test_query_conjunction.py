import unittest

from dt.client.dgraph.constants.comparison_function import ComparisonFunction
from dt.client.dgraph.constants.query_conjunction_type import \
    QueryConjunctionType
from dt.client.dgraph.dql.query_conjunction import QueryConjunction
from dt.client.dgraph.dql.query_function import QueryFunction
from dt.client.dgraph.graphql.value import Value

TEST_ARG_1 = "TEST_ARG_1"
TEST_ARG_2 = "TEST_ARG_2"
TEST_COMPARISON_FUNCTION = ComparisonFunction.EQ
TEST_COMPARISON_FUNCTION_2 = ComparisonFunction.LE
TEST_QUERY_CONJUNCTION = QueryConjunctionType.AND
TEST_QUERY_CONJUNCTION_2 = QueryConjunctionType.NOT
TEST_GRAPHQL_STR_NOT = "(NOT eq(TEST_ARG_1, TEST_ARG_2))"
TEST_GRAPHQL_STR_AND = "(eq(TEST_ARG_1, TEST_ARG_2) AND le(TEST_ARG_1, TEST_ARG_2))"


class QueryConjunctionTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        query_function_args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, query_function_args)
        query_function2 = QueryFunction(TEST_COMPARISON_FUNCTION_2, query_function_args)
        conjunction_args = (query_function, query_function2)
        query_conjunction = QueryConjunction(TEST_QUERY_CONJUNCTION, conjunction_args)
        self.assertEqual(query_conjunction.comp_func, TEST_QUERY_CONJUNCTION)
        self.assertEqual(query_conjunction.args, conjunction_args)

    def test_to_graphql_not(self) -> None:
        query_function_args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, query_function_args)
        conjunction_args = (query_function,)
        query_conjunction = QueryConjunction(TEST_QUERY_CONJUNCTION_2, conjunction_args)
        expected = TEST_GRAPHQL_STR_NOT
        actual = query_conjunction.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_and(self) -> None:
        query_function_args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, query_function_args)
        query_function2 = QueryFunction(TEST_COMPARISON_FUNCTION_2, query_function_args)
        conjunction_args = (query_function, query_function2)
        query_conjunction = QueryConjunction(TEST_QUERY_CONJUNCTION, conjunction_args)
        expected = TEST_GRAPHQL_STR_AND
        actual = query_conjunction.to_graphql()
        self.assertEqual(actual, expected)
