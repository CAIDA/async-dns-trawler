import unittest

from dt.client.dgraph.constants.comparison_function import ComparisonFunction
from dt.client.dgraph.error.invalid_comparison_function_error import \
    InvalidComparisonFunctionError
from dt.client.dgraph.mapper.comparison_function_mapper import \
    ComparisonFunctionMapper
from dt.dns_trawler.constants.query_operator import QueryOperator


class ComparisonFunctionMapperTestCase(unittest.TestCase):

    def test_is_comparision_function_true(self) -> None:
        actual = ComparisonFunctionMapper.is_comparison_function(QueryOperator.EQ)
        self.assertTrue(actual)

    def test_is_comparision_function_false(self) -> None:
        actual = ComparisonFunctionMapper.is_comparison_function(QueryOperator.AND)
        self.assertFalse(actual)

    def test_from_query_operator_successful(self) -> None:
        expected = ComparisonFunction.EQ
        actual = ComparisonFunctionMapper.from_query_operator(QueryOperator.EQ)
        self.assertEqual(actual, expected)

    def test_from_query_operator_error(self) -> None:
        def convert() -> None:
            ComparisonFunctionMapper.from_query_operator(QueryOperator.AND)
        self.assertRaises(InvalidComparisonFunctionError, convert)
