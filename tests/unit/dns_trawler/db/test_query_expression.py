import unittest

from dt.dns_trawler.constants.query_operator import QueryOperator
from dt.dns_trawler.db.query_expression import QueryExpression
from dt.dns_trawler.db.query_field import QueryField
from dt.dns_trawler.error.invalid_query_error import InvalidQueryError

TEST_QUERY_OPERATOR = QueryOperator.EQ
TEST_QUERY_OPERATOR_2 = QueryOperator.LE
TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_FIELD_VALUE = "TEST_FIELD_VALUE"
TEST_FIELD_NAME_2 = "TEST_FIELD_NAME_2"
TEST_FIELD_VALUE_2 = "TEST_FIELD_VALUE_2"
TEST_REPR = "EQ(QueryField(TEST_FIELD_NAME), 'TEST_FIELD_VALUE')"


class QueryExpressionTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        self.assertEqual(query_expression.args, query_expression_args)
        self.assertEqual(query_expression.query_operator, TEST_QUERY_OPERATOR)

    def test_repr(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        actual = repr(query_expression)
        expected = TEST_REPR
        self.assertEqual(actual, expected)

    def test_eq_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_field_2 = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression_args_2 = (query_field_2, TEST_FIELD_VALUE)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        query_expression_2 = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args_2)
        self.assertEqual(query_expression, query_expression_2)

    def test_eq_different_query_operator(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_field_2 = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression_args_2 = (query_field_2, TEST_FIELD_VALUE)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        query_expression_2 = QueryExpression(QueryOperator.OR, query_expression_args_2)
        self.assertNotEqual(query_expression, query_expression_2)

    def test_eq_different_args(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression_args_2 = (query_field, TEST_FIELD_VALUE_2)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        query_expression_2 = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args_2)
        self.assertNotEqual(query_expression, query_expression_2)

    def test_eq_different_class(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        query_expression_2 = object()
        self.assertNotEqual(query_expression, query_expression_2)

    def test_and_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_field_2 = QueryField(TEST_FIELD_NAME_2)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression_args_2 = (query_field_2, TEST_FIELD_VALUE_2)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        query_expression_2 = QueryExpression(TEST_QUERY_OPERATOR_2, query_expression_args_2)
        actual = query_expression & query_expression_2
        expected = QueryExpression(QueryOperator.AND, (query_expression, query_expression_2))
        self.assertEqual(actual, expected)

    def test_and_error(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        other = object()

        def and_operation() -> None:
            actual = query_expression & other
        self.assertRaises(InvalidQueryError, and_operation)

    def test_or_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_field_2 = QueryField(TEST_FIELD_NAME_2)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression_args_2 = (query_field_2, TEST_FIELD_VALUE_2)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        query_expression_2 = QueryExpression(TEST_QUERY_OPERATOR_2, query_expression_args_2)
        actual = query_expression | query_expression_2
        expected = QueryExpression(QueryOperator.OR, (query_expression, query_expression_2))
        self.assertEqual(actual, expected)

    def test_or_error(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        other = object()

        def or_operation() -> None:
            actual = query_expression | other
        self.assertRaises(InvalidQueryError, or_operation)

    def test_not_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_expression_args = (query_field, TEST_FIELD_VALUE)
        query_expression = QueryExpression(TEST_QUERY_OPERATOR, query_expression_args)
        actual = ~query_expression
        expected = QueryExpression(QueryOperator.NOT, (query_expression,))
        self.assertEqual(actual, expected)
