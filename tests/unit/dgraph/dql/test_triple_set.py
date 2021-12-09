import unittest

from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.dgraph.dql.triple import Triple
from dt.dgraph.dql.triple_set import TripleSet

TEST_UID = "0x1"
TEST_UID_2 = "0x2"
TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_STRING_PREDICATE_VALUE = "TEST_STRING_PREDICATE_VALUE"
TEST_NQUAD_STATEMENT = '<0x1> <TEST_PREDICATE_NAME> "TEST_STRING_PREDICATE_VALUE"^^<xs:string> .\n' + \
                       '<0x2> <TEST_PREDICATE_NAME> "TEST_STRING_PREDICATE_VALUE"^^<xs:string> .'


class TripleSetTestCase(unittest.TestCase):
    def test_constructor_no_iterable(self) -> None:
        triple_set = TripleSet()
        self.assertEqual(triple_set, set())

    def test_constructor_with_iterable(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple = Triple(node_id, predicate)
        triple_set = TripleSet({triple})
        self.assertEqual(triple_set, {triple})

    def test_to_nquad_statement(self) -> None:
        node_id = NodeId(TEST_UID)
        node_id2 = NodeId(TEST_UID_2)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        triple = Triple(node_id, predicate)
        triple2 = Triple(node_id2, predicate)
        triple_set = TripleSet({triple, triple2})
        self.assertEqual(triple_set.to_nquad_statement(), TEST_NQUAD_STATEMENT)
