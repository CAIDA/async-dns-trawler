import unittest

from dt.client.dgraph.dql.predicate import Predicate

TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_STRING_PREDICATE_VALUE = "TEST_STRING_PREDICATE_VALUE"
TEST_INT_PREDICATE_VALUE = 99
TEST_INT_PREDICATE_VALUE_STR = "99"
TEST_INT_PREDICATE_REPR = "Predicate(TEST_PREDICATE_NAME, 99)"
TEST_INT_PREDICATE_NQUAD_STATEMENT = '<TEST_PREDICATE_NAME> "99"'


class PredicateTestCase(unittest.TestCase):
    def test_constructor_string_predicate(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE)
        self.assertEqual(predicate.predicate_name, TEST_PREDICATE_NAME)
        self.assertEqual(predicate.predicate_value, TEST_STRING_PREDICATE_VALUE)

    def test_constructor_int_predicate(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        self.assertEqual(predicate.predicate_name, TEST_PREDICATE_NAME)
        self.assertEqual(predicate.predicate_value, TEST_INT_PREDICATE_VALUE_STR)

    def test_hash_equal_same_value(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        predicate2 = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        self.assertEqual(hash(predicate), hash(predicate2))

    def test_hash_equal_different_value_datatype(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        predicate2 = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE_STR)
        self.assertEqual(hash(predicate), hash(predicate2))

    def test_hash_not_equal(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        predicate2 = Predicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE)
        self.assertNotEqual(hash(predicate), hash(predicate2))

    def test_eq_equal_same_value(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        predicate2 = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        self.assertEqual(predicate, predicate2)

    def test_eq_equal_different_value_datatype(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        predicate2 = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE_STR)
        self.assertEqual(hash(predicate), hash(predicate2))

    def test_eq_not_equal(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        predicate2 = Predicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE)
        self.assertNotEqual(predicate, predicate2)

    def test_eq_not_equal_different_class(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        predicate2 = object()
        self.assertNotEqual(predicate, predicate2)

    def test_repr(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        self.assertEqual(repr(predicate), TEST_INT_PREDICATE_REPR)

    def test_to_nquad_statement(self) -> None:
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE)
        self.assertEqual(predicate.to_nquad_statement(), TEST_INT_PREDICATE_NQUAD_STATEMENT)
