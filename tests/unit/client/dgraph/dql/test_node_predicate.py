import unittest

from dt.client.dgraph.dql.blank_node_id import BlankNodeId
from dt.client.dgraph.dql.node_id import NodeId
from dt.client.dgraph.dql.node_predicate import NodePredicate

TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_UID = "0x1"
TEST_UID_2 = "TEST_UID2"
TEST_PREDICATE_VALUE = "<0x1>"
TEST_REPR = "NodePredicate(TEST_PREDICATE_NAME, <0x1>)"
TEST_NQUAD_STATEMENT_1 = "<TEST_PREDICATE_NAME> <0x1>"
TEST_NQUAD_STATEMENT_2 = "<TEST_PREDICATE_NAME> _:TEST_UID2"


class NodePredicateTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        self.assertEqual(predicate.predicate_name, TEST_PREDICATE_NAME)
        self.assertEqual(predicate.predicate_value, TEST_PREDICATE_VALUE)

    def test_hash_equal_same_node_id(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        predicate2 = NodePredicate(TEST_PREDICATE_NAME, node_id)
        self.assertEqual(hash(predicate), hash(predicate2))

    def test_hash_equal_same_blank_node_id(self) -> None:
        blank_node_id = BlankNodeId(TEST_UID)
        predicate = NodePredicate(TEST_PREDICATE_NAME, blank_node_id)
        predicate2 = NodePredicate(TEST_PREDICATE_NAME, blank_node_id)
        self.assertEqual(hash(predicate), hash(predicate2))

    def test_hash_not_equal(self) -> None:
        node_id = NodeId(TEST_UID)
        node_id2 = BlankNodeId(TEST_UID_2)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        predicate2 = NodePredicate(TEST_PREDICATE_NAME, node_id2)
        self.assertNotEqual(hash(predicate), hash(predicate2))

    def test_eq_equal_same_node_id(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        predicate2 = NodePredicate(TEST_PREDICATE_NAME, node_id)
        self.assertEqual(predicate, predicate2)

    def test_eq_equal_same_blank_node_id(self) -> None:
        blank_node_id = BlankNodeId(TEST_UID)
        predicate = NodePredicate(TEST_PREDICATE_NAME, blank_node_id)
        predicate2 = NodePredicate(TEST_PREDICATE_NAME, blank_node_id)
        self.assertEqual(predicate, predicate2)

    def test_eq_not_equal(self) -> None:
        node_id = NodeId(TEST_UID)
        node_id2 = BlankNodeId(TEST_UID_2)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        predicate2 = NodePredicate(TEST_PREDICATE_NAME, node_id2)
        self.assertNotEqual(predicate, predicate2)

    def test_eq_not_equal_different_class(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        predicate2 = object()
        self.assertNotEqual(predicate, predicate2)

    def test_repr(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        self.assertEqual(repr(predicate), TEST_REPR)

    def test_to_nquad_statement_node_id(self) -> None:
        node_id = NodeId(TEST_UID)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        self.assertEqual(predicate.to_nquad_statement(), TEST_NQUAD_STATEMENT_1)

    def test_to_nquad_statement_blank_node_id(self) -> None:
        node_id = BlankNodeId(TEST_UID_2)
        predicate = NodePredicate(TEST_PREDICATE_NAME, node_id)
        self.assertEqual(predicate.to_nquad_statement(), TEST_NQUAD_STATEMENT_2)
