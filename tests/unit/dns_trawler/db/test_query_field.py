import unittest

from dt.dns_trawler.constants.query_operator import QueryOperator
from dt.dns_trawler.db.query_expression import QueryExpression
from dt.dns_trawler.db.query_field import QueryField
from dt.dns_trawler.error.invalid_query_error import InvalidQueryError

TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_FIELD_NAME_2 = "TEST_FIELD_NAME_2"
TEST_FIELD_VALUE = "TEST_FIELD_VALUE"
TEST_FIELD_VALUE_INVALID = object()
TEST_REPR = "QueryField(TEST_FIELD_NAME)"


class QueryFieldTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        self.assertEqual(TEST_FIELD_NAME, query_field.field_name)

    def test_repr(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        actual = repr(query_field)
        expected = TEST_REPR
        self.assertEqual(actual, expected)

    def test_eq_magic_method_same_value(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_field_2 = QueryField(TEST_FIELD_NAME)
        self.assertEqual(query_field, query_field_2)

    def test_eq_magic_method_different_value(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_field_2 = QueryField(TEST_FIELD_NAME_2)
        self.assertNotEqual(query_field, query_field_2)

    def test_eq_magic_method_different_class(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_field_2 = object()
        self.assertNotEqual(query_field, query_field_2)

    def test_eq_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        actual = query_field.eq(TEST_FIELD_VALUE)
        expected = QueryExpression(QueryOperator.EQ, (query_field, TEST_FIELD_VALUE))
        self.assertEqual(actual, expected)

    def test_eq_error(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)

        def eq_operation() -> None:
            query_field.eq(TEST_FIELD_VALUE_INVALID)
        self.assertRaises(InvalidQueryError, eq_operation)

    def test_ne_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        actual = query_field.ne(TEST_FIELD_VALUE)
        expected = QueryExpression(QueryOperator.NE, (query_field, TEST_FIELD_VALUE))
        self.assertEqual(actual, expected)

    def test_ne_error(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)

        def ne_operation() -> None:
            query_field.ne(TEST_FIELD_VALUE_INVALID)
        self.assertRaises(InvalidQueryError, ne_operation)

    def test_lt_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        actual = query_field.lt(TEST_FIELD_VALUE)
        expected = QueryExpression(QueryOperator.LT, (query_field, TEST_FIELD_VALUE))
        self.assertEqual(actual, expected)

    def test_lt_error(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)

        def lt_operation() -> None:
            query_field.lt(TEST_FIELD_VALUE_INVALID)
        self.assertRaises(InvalidQueryError, lt_operation)

    def test_le_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        actual = query_field.le(TEST_FIELD_VALUE)
        expected = QueryExpression(QueryOperator.LE, (query_field, TEST_FIELD_VALUE))
        self.assertEqual(actual, expected)

    def test_le_error(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)

        def le_operation() -> None:
            query_field.le(TEST_FIELD_VALUE_INVALID)
        self.assertRaises(InvalidQueryError, le_operation)

    def test_gt_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        actual = query_field.gt(TEST_FIELD_VALUE)
        expected = QueryExpression(QueryOperator.GT, (query_field, TEST_FIELD_VALUE))
        self.assertEqual(actual, expected)

    def test_gt_error(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)

        def gt_operation() -> None:
            query_field.gt(TEST_FIELD_VALUE_INVALID)
        self.assertRaises(InvalidQueryError, gt_operation)

    def test_ge_successful(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        actual = query_field.ge(TEST_FIELD_VALUE)
        expected = QueryExpression(QueryOperator.GE, (query_field, TEST_FIELD_VALUE))
        self.assertEqual(actual, expected)

    def test_ge_error(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)

        def ge_operation() -> None:
            query_field.ge(TEST_FIELD_VALUE_INVALID)
        self.assertRaises(InvalidQueryError, ge_operation)
