import unittest

from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.triple import Triple

TEST_UID = "0x1"
TEST_UID_2 = "0x2"
TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_STRING_PREDICATE_VALUE = "TEST_STRING_PREDICATE_VALUE"
TEST_NQUAD_STATEMENT = '<0x1> <TEST_PREDICATE_NAME> "TEST_STRING_PREDICATE_VALUE"^^<xs:string> .'


class TripleTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple = Triple(node_id, predicate)
        self.assertEqual(triple.subject, node_id)
        self.assertEqual(triple.predicate, predicate)

    def test_hash_equal(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple1 = Triple(node_id, predicate)
        triple2 = Triple(node_id, predicate)
        self.assertEqual(hash(triple1), hash(triple2))

    def test_hash_not_equal(self) -> None:
        node_id_1 = NodeId(TEST_UID)
        node_id_2 = NodeId(TEST_UID_2)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple1 = Triple(node_id_1, predicate)
        triple2 = Triple(node_id_2, predicate)
        self.assertNotEqual(hash(triple1), hash(triple2))

    def test_eq_equal(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple1 = Triple(node_id, predicate)
        triple2 = Triple(node_id, predicate)
        self.assertEqual(triple1, triple2)

    def test_eq_not_equal(self) -> None:
        node_id_1 = NodeId(TEST_UID)
        node_id_2 = NodeId(TEST_UID_2)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple1 = Triple(node_id_1, predicate)
        triple2 = Triple(node_id_2, predicate)
        self.assertNotEqual(triple1, triple2)

    def test_eq_not_equal_different_class(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple1 = Triple(node_id, predicate)
        triple2 = object()
        self.assertNotEqual(triple1, triple2)

    def test_to_nquad_statement(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple = Triple(node_id, predicate)
        self.assertEqual(triple.to_nquad_statement(), TEST_NQUAD_STATEMENT)
