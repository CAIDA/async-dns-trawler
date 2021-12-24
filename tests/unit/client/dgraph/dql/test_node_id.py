import unittest

from dt.client.dgraph.dql.node_id import NodeId

TEST_UID = "0x1"
TEST_UID_2 = "0x2"
TEST_REPR = "0x1"
TEST_NQUAD_STATEMENT = "<0x1>"


class NodeIdTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        node_id = NodeId(TEST_UID)
        self.assertEqual(node_id.value, TEST_UID)

    def test_hash_equal(self) -> None:
        node_id = NodeId(TEST_UID)
        node_id2 = NodeId(TEST_UID)
        self.assertEqual(hash(node_id), hash(node_id2))

    def test_hash_not_equal(self) -> None:
        node_id = NodeId(TEST_UID)
        node_id2 = NodeId(TEST_UID_2)
        self.assertNotEqual(hash(node_id), hash(node_id2))

    def test_eq_equal(self) -> None:
        node_id = NodeId(TEST_UID)
        node_id2 = NodeId(TEST_UID)
        self.assertEqual(node_id, node_id2)

    def test_eq_not_equal(self) -> None:
        node_id = NodeId(TEST_UID)
        node_id2 = NodeId(TEST_UID_2)
        self.assertNotEqual(node_id, node_id2)

    def test_eq_not_equal_different_class(self) -> None:
        node_id = NodeId(TEST_UID)
        node_id2 = object()
        self.assertNotEqual(node_id, node_id2)

    def test_repr(self) -> None:
        node_id = NodeId(TEST_UID)
        self.assertEqual(repr(node_id), TEST_REPR)

    def test_to_nquad_statement(self) -> None:
        node_id = NodeId(TEST_UID)
        self.assertEqual(node_id.to_nquad_statement(), TEST_NQUAD_STATEMENT)
