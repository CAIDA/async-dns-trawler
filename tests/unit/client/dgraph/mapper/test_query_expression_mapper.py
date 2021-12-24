import typing
import unittest
from enum import Enum

from dt.client.dgraph.constants.comparison_function import ComparisonFunction
from dt.client.dgraph.constants.query_conjunction_type import \
    QueryConjunctionType
from dt.client.dgraph.dql.query_conjunction import QueryConjunction
from dt.client.dgraph.dql.query_function import QueryFunction
from dt.client.dgraph.error.invalid_query_expression_error import \
    InvalidQueryExpressionError
from dt.client.dgraph.graphql.value import Value
from dt.client.dgraph.mapper.query_expression_mapper import \
    QueryExpressionMapper
from dt.dns_trawler.constants.query_operator import QueryOperator
from dt.dns_trawler.db.query_expression import QueryExpression
from dt.dns_trawler.db.query_field import QueryField

TEST_FIELD_NAME = 'TEST_FIELD_NAME'
TEST_FIELD_VALUE = 'TEST_FIELD_VALUE'
TEST_FIELD_NAME_2 = 'TEST_FIELD_NAME_2'
TEST_FIELD_VALUE_2 = 'TEST_FIELD_VALUE_2'


class InvalidQueryOperator(Enum):
    INVALID = "invalid"


class QueryExpressionMapperTestCase(unittest.TestCase):
    def test_to_query_function_single_comparison(self) -> None:
        expected = QueryFunction(ComparisonFunction.EQ, (Value(TEST_FIELD_NAME), Value(TEST_FIELD_VALUE)))
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression = query_field.eq(TEST_FIELD_VALUE)
        actual = QueryExpressionMapper.to_query_function(query_expression)
        self.assertEqual(actual, expected)

    def test_to_query_function_nested_comparisons(self) -> None:
        expected = QueryConjunction(QueryConjunctionType.OR, (
            QueryFunction(
                ComparisonFunction.EQ, (
                    Value(TEST_FIELD_NAME),
                    Value(TEST_FIELD_VALUE)
                )
            ),
            QueryFunction(
                ComparisonFunction.LE, (
                    Value(TEST_FIELD_NAME_2),
                    Value(TEST_FIELD_VALUE_2)
                )
            )))
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression = query_field.eq(TEST_FIELD_VALUE)
        query_field_2 = QueryField(TEST_FIELD_NAME_2)
        query_expression_2 = query_field_2.le(TEST_FIELD_VALUE_2)
        combined_query_expression = query_expression | query_expression_2
        actual = QueryExpressionMapper.to_query_function(combined_query_expression)
        self.assertEqual(actual, expected)

    def test_to_query_function_with_ne(self) -> None:
        expected = QueryConjunction(QueryConjunctionType.NOT, (
            QueryFunction(
                ComparisonFunction.EQ, (
                    Value(TEST_FIELD_NAME),
                    Value(TEST_FIELD_VALUE)
                )
            ),))
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression = query_field.ne(TEST_FIELD_VALUE)
        actual = QueryExpressionMapper.to_query_function(query_expression)
        self.assertEqual(actual, expected)

    def test_to_query_function_error(self) -> None:
        operator = typing.cast(QueryOperator, InvalidQueryOperator.INVALID)
        expression = QueryExpression(operator, (TEST_FIELD_NAME, TEST_FIELD_VALUE))

        def to_query_function() -> None:
            QueryExpressionMapper.to_query_function(expression)
        self.assertRaises(InvalidQueryExpressionError, to_query_function)
