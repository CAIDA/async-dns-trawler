import unittest

from dt.client.dgraph.constants.query_conjunction_type import \
    QueryConjunctionType
from dt.client.dgraph.error.invalid_query_conjunction_type_error import \
    InvalidQueryConjunctionTypeError
from dt.client.dgraph.mapper.query_conjunction_type_mapper import \
    QueryConjunctionTypeMapper
from dt.dns_trawler.constants.query_operator import QueryOperator


class QueryConjunctionTypeMapperTestCase(unittest.TestCase):

    def test_is_query_conjunction_type_true(self) -> None:
        actual = QueryConjunctionTypeMapper.is_query_conjunction_type(QueryOperator.AND)
        self.assertTrue(actual)

    def test_is_query_conjunction_type_false(self) -> None:
        actual = QueryConjunctionTypeMapper.is_query_conjunction_type(QueryOperator.EQ)
        self.assertFalse(actual)

    def test_from_query_operator_successful(self) -> None:
        expected = QueryConjunctionType.AND
        actual = QueryConjunctionTypeMapper.from_query_operator(QueryOperator.AND)
        self.assertEqual(actual, expected)

    def test_from_query_operator_error(self) -> None:
        def convert() -> None:
            QueryConjunctionTypeMapper.from_query_operator(QueryOperator.EQ)
        self.assertRaises(InvalidQueryConjunctionTypeError, convert)
