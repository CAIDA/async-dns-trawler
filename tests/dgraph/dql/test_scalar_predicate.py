import unittest

from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.dql.scalar_predicate import ScalarPredicate

TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_STRING_PREDICATE_VALUE = "TEST_STRING_PREDICATE_VALUE"
TEST_ALT_STRING_PREDICATE_VALUE = "TEST_ALT_STRING_PREDICATE_VALUE"
TEST_INT_PREDICATE_VALUE = 99
TEST_INT_PREDICATE_VALUE_STR = "99"
TEST_INT_PREDICATE_REPR = "ScalarPredicate(TEST_PREDICATE_NAME, 99, ScalarType.INT)"
TEST_INT_PREDICATE_NQUAD_STATEMENT = '<TEST_PREDICATE_NAME> "99"^^<xs:int>'
TEST_STRING_PREDICATE_NQUAD_STATEMENT = '<TEST_PREDICATE_NAME> "99"^^<xs:string>'


class ScalarPredicateTestCase(unittest.TestCase):
    def test_constructor_string_predicate(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        self.assertEqual(predicate.predicate_name, TEST_PREDICATE_NAME)
        self.assertEqual(predicate.predicate_type, ScalarType.STRING)
        self.assertEqual(predicate.predicate_value,
                         TEST_STRING_PREDICATE_VALUE)

    def test_constructor_int_predicate(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        self.assertEqual(predicate.predicate_name, TEST_PREDICATE_NAME)
        self.assertEqual(predicate.predicate_type, ScalarType.INT)
        self.assertEqual(predicate.predicate_value,
                         TEST_INT_PREDICATE_VALUE_STR)

    def test_hash_equal(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        predicate2 = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        self.assertEqual(hash(predicate), hash(predicate2))

    def test_hash_not_equal_different_datatype(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        predicate2 = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE_STR, ScalarType.STRING)
        self.assertNotEqual(hash(predicate), hash(predicate2))

    def test_hash_not_equal(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        predicate2 = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        self.assertNotEqual(hash(predicate), hash(predicate2))

    def test_eq_equal(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        predicate2 = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        self.assertEqual(predicate, predicate2)

    def test_eq_not_equal_different_datatype(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        predicate2 = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE_STR, ScalarType.STRING)
        self.assertNotEqual(predicate, predicate2)

    def test_eq_not_equal(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        predicate2 = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        self.assertNotEqual(predicate, predicate2)

    def test_repr(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        self.assertEqual(repr(predicate), TEST_INT_PREDICATE_REPR)

    def test_to_nquad_statement_int(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        self.assertEqual(predicate.to_nquad_statement(),
                         TEST_INT_PREDICATE_NQUAD_STATEMENT)

    def test_to_nquad_statement_string(self) -> None:
        predicate = ScalarPredicate(
            TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE_STR, ScalarType.STRING)
        self.assertEqual(predicate.to_nquad_statement(),
                         TEST_STRING_PREDICATE_NQUAD_STATEMENT)
