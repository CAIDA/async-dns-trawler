import unittest

from dt.client.dgraph.constants.scalar_type import ScalarType
from dt.client.dgraph.dql.node_id import NodeId
from dt.client.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.client.dgraph.dql.triple import Triple
from dt.client.dgraph.entity.node import Node

TEST_UID = "0x1"
TEST_UID_2 = "0x2"
TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_INT_PREDICATE_VALUE = 99
TEST_STRING_PREDICATE_VALUE = "TEST_STRING_PREDICATE_VALUE"
TEST_NODE_REPR = "Node(0x1)"


class NodeTestCase(unittest.TestCase):

    def test_constructor(self) -> None:
        node = Node(TEST_UID)
        self.assertEqual(node.predicates, set())

    def test_add_predicate(self) -> None:
        node = Node(TEST_UID)
        self.assertEqual(len(node.predicates), 0)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        node.add_predicate(predicate)
        self.assertEqual(len(node.predicates), 1)

    def test_hash_equal_no_predicates(self) -> None:
        node = Node(TEST_UID)
        node2 = Node(TEST_UID)
        self.assertEqual(hash(node), hash(node2))

    def test_hash_not_equal_no_predicates(self) -> None:
        node = Node(TEST_UID)
        node2 = Node(TEST_UID_2)
        self.assertNotEqual(hash(node), hash(node2))

    def test_hash_equal_with_predicates(self) -> None:
        node = Node(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        node.add_predicate(predicate)

        node2 = Node(TEST_UID)
        predicate2 = ScalarPredicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        node2.add_predicate(predicate2)
        self.assertEqual(hash(node), hash(node2))

    def test_hash_not_equal_with_predicates(self) -> None:
        node = Node(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        node.add_predicate(predicate)

        node2 = Node(TEST_UID)
        predicate2 = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        node2.add_predicate(predicate2)
        self.assertNotEqual(hash(node), hash(node2))

    def test_eq_equal_no_predicates(self) -> None:
        node = Node(TEST_UID)
        node2 = Node(TEST_UID)
        self.assertEqual(node, node2)

    def test_eq_not_equal_no_predicates(self) -> None:
        node = Node(TEST_UID)
        node2 = Node(TEST_UID_2)
        self.assertNotEqual(node, node2)

    def test_eq_equal_with_predicates(self) -> None:
        node = Node(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        node.add_predicate(predicate)

        node2 = Node(TEST_UID)
        predicate2 = ScalarPredicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        node2.add_predicate(predicate2)
        self.assertEqual(node, node2)

    def test_eq_not_equal_with_predicates(self) -> None:
        node = Node(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        node.add_predicate(predicate)

        node2 = Node(TEST_UID)
        predicate2 = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        node2.add_predicate(predicate2)
        self.assertNotEqual(node, node2)

    def test_eq_not_equal_different_class(self) -> None:
        node = Node(TEST_UID)
        node2 = object()
        self.assertNotEqual(node, node2)

    def test_repr(self) -> None:
        node = Node(TEST_UID)
        self.assertEqual(repr(node), TEST_NODE_REPR)

    def test_to_dql_triples(self) -> None:
        node = Node(TEST_UID)
        predicate = ScalarPredicate(TEST_PREDICATE_NAME, TEST_INT_PREDICATE_VALUE, ScalarType.INT)
        predicate2 = ScalarPredicate(TEST_PREDICATE_NAME, TEST_STRING_PREDICATE_VALUE, ScalarType.STRING)
        node.add_predicate(predicate)
        node.add_predicate(predicate2)
        expected = {
            Triple(NodeId(TEST_UID), predicate),
            Triple(NodeId(TEST_UID), predicate2),
        }
        self.assertEqual(node.to_dql_triples(), expected)
