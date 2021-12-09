import unittest

from dt.dns_trawler.constants.query_operator import QueryOperator
from dt.dns_trawler.constants.sort_direction import SortDirection
from dt.dns_trawler.db.query_expression import QueryExpression
from dt.dns_trawler.db.query_field import QueryField
from dt.dns_trawler.db.query_options import QueryOptions

TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_FIELD_VALUE = "TEST_FIELD_VALUE"
TEST_QUERY_FIELD = QueryField(TEST_FIELD_NAME)
TEST_QUERY_EXPRESSION = QueryExpression(QueryOperator.EQ, (
    TEST_QUERY_FIELD,
    TEST_FIELD_VALUE
))
TEST_SORT_DIRECTION = SortDirection.ASC
TEST_NEXT_TOKEN = "TEST_NEXT_TOKEN"
TEST_MAX_RESULTS = 5
TEST_REPR_1 = "QueryOptions(expression=EQ(QueryField(TEST_FIELD_NAME), 'TEST_FIELD_VALUE'))"
TEST_REPR_2 = "QueryOptions(expression=EQ(QueryField(TEST_FIELD_NAME), 'TEST_FIELD_VALUE'), " + \
    "max_results=5)"
TEST_REPR_3 = "QueryOptions(expression=EQ(QueryField(TEST_FIELD_NAME), 'TEST_FIELD_VALUE'), " + \
    "next_token=TEST_NEXT_TOKEN)"
TEST_REPR_4 = "QueryOptions(expression=EQ(QueryField(TEST_FIELD_NAME), 'TEST_FIELD_VALUE'), " + \
    "sort_direction=ASC)"
TEST_REPR_5 = "QueryOptions(expression=EQ(QueryField(TEST_FIELD_NAME), 'TEST_FIELD_VALUE'), " + \
    "max_results=5, " + \
    "next_token=TEST_NEXT_TOKEN, " + \
    "sort_direction=ASC)"


class QueryOptionsTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        query_options = QueryOptions(expression=TEST_QUERY_EXPRESSION,
                                     max_results=TEST_MAX_RESULTS,
                                     next_token=TEST_NEXT_TOKEN,
                                     sort_direction=TEST_SORT_DIRECTION)
        self.assertEqual(query_options.expression, TEST_QUERY_EXPRESSION)
        self.assertEqual(query_options.max_results, TEST_MAX_RESULTS)
        self.assertEqual(query_options.next_token, TEST_NEXT_TOKEN)
        self.assertEqual(query_options.sort_direction, TEST_SORT_DIRECTION)

    def test_repr_only_expression(self) -> None:
        query_options = QueryOptions(expression=TEST_QUERY_EXPRESSION)
        actual = repr(query_options)
        expected = TEST_REPR_1
        self.assertEqual(actual, expected)

    def test_repr_expression_with_max_results(self) -> None:
        query_options = QueryOptions(expression=TEST_QUERY_EXPRESSION,
                                     max_results=TEST_MAX_RESULTS)
        actual = repr(query_options)
        expected = TEST_REPR_2
        self.assertEqual(actual, expected)

    def test_repr_expression_with_next_token(self) -> None:
        query_options = QueryOptions(expression=TEST_QUERY_EXPRESSION,
                                     next_token=TEST_NEXT_TOKEN)
        actual = repr(query_options)
        expected = TEST_REPR_3
        self.assertEqual(actual, expected)

    def test_repr_expression_with_sort_direction(self) -> None:
        query_options = QueryOptions(expression=TEST_QUERY_EXPRESSION,
                                     sort_direction=TEST_SORT_DIRECTION)
        actual = repr(query_options)
        expected = TEST_REPR_4
        self.assertEqual(actual, expected)

    def test_repr_full(self) -> None:
        query_options = QueryOptions(expression=TEST_QUERY_EXPRESSION,
                                     max_results=TEST_MAX_RESULTS,
                                     next_token=TEST_NEXT_TOKEN,
                                     sort_direction=TEST_SORT_DIRECTION)
        actual = repr(query_options)
        expected = TEST_REPR_5
        self.assertEqual(actual, expected)
