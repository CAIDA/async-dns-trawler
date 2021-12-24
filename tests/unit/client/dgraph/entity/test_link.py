import unittest

from dt.client.dgraph.dql.node_id import NodeId
from dt.client.dgraph.dql.node_predicate import NodePredicate
from dt.client.dgraph.dql.triple import Triple
from dt.client.dgraph.entity.link import Link
from dt.client.dgraph.entity.node import Node

TEST_UID = "0x1"
TEST_UID_2 = "0x2"
TEST_LINK_TYPE = "TEST_LINK_TYPE"
TEST_LINK_REPR = "Link(TEST_LINK_TYPE, source=0x1, target=0x2)"


class LinkTestCase(unittest.TestCase):

    def test_constructor(self) -> None:
        source = Node(TEST_UID)
        target = Node(TEST_UID_2)
        link = Link(TEST_LINK_TYPE, source, target)
        self.assertEqual(link.link_type, TEST_LINK_TYPE)
        self.assertEqual(link.source, source)
        self.assertEqual(link.target, target)

    def test_hash_equal(self) -> None:
        source = Node(TEST_UID)
        target = Node(TEST_UID_2)
        link = Link(TEST_LINK_TYPE, source, target)
        link2 = Link(TEST_LINK_TYPE, source, target)
        self.assertEqual(hash(link), hash(link2))

    def test_hash_not_equal(self) -> None:
        source = Node(TEST_UID)
        target = Node(TEST_UID_2)
        link = Link(TEST_LINK_TYPE, source, target)
        link2 = Link(TEST_LINK_TYPE, source, source)
        self.assertNotEqual(hash(link), hash(link2))

    def test_eq_equal(self) -> None:
        source = Node(TEST_UID)
        target = Node(TEST_UID_2)
        link = Link(TEST_LINK_TYPE, source, target)
        link2 = Link(TEST_LINK_TYPE, source, target)
        self.assertEqual(link, link2)

    def test_eq_not_equal(self) -> None:
        source = Node(TEST_UID)
        target = Node(TEST_UID_2)
        link = Link(TEST_LINK_TYPE, source, target)
        link2 = Link(TEST_LINK_TYPE, source, source)
        self.assertNotEqual(link, link2)

    def test_eq_not_equal_different_class(self) -> None:
        source = Node(TEST_UID)
        target = Node(TEST_UID_2)
        link = Link(TEST_LINK_TYPE, source, target)
        link2 = object()
        self.assertNotEqual(link, link2)

    def test_repr(self) -> None:
        source = Node(TEST_UID)
        target = Node(TEST_UID_2)
        link = Link(TEST_LINK_TYPE, source, target)
        self.assertEqual(repr(link), TEST_LINK_REPR)

    def test_to_dql_triples(self) -> None:
        source = Node(TEST_UID)
        target = Node(TEST_UID_2)
        link = Link(TEST_LINK_TYPE, source, target)
        node_predicate = NodePredicate(TEST_LINK_TYPE, NodeId(TEST_UID_2))
        expected = {Triple(NodeId(TEST_UID), node_predicate)}
        self.assertEqual(link.to_dql_triples(), expected)
