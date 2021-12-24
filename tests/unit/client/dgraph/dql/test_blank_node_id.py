import unittest

from dt.client.dgraph.dql.blank_node_id import BlankNodeId

TEST_UID = "TEST_UID"
TEST_UID_2 = "TEST_UID2"
TEST_REPR = "TEST_UID"
TEST_NQUAD_STATEMENT = "_:TEST_UID"


class BlankNodeIdTestCase(unittest.TestCase):
    def test_hash_equal(self) -> None:
        node_id = BlankNodeId(TEST_UID)
        node_id2 = BlankNodeId(TEST_UID)
        self.assertEqual(hash(node_id), hash(node_id2))

    def test_hash_not_equal(self) -> None:
        node_id = BlankNodeId(TEST_UID)
        node_id2 = BlankNodeId(TEST_UID_2)
        self.assertNotEqual(hash(node_id), hash(node_id2))

    def test_eq_equal(self) -> None:
        node_id = BlankNodeId(TEST_UID)
        node_id2 = BlankNodeId(TEST_UID)
        self.assertEqual(node_id, node_id2)

    def test_eq_not_equal(self) -> None:
        node_id = BlankNodeId(TEST_UID)
        node_id2 = BlankNodeId(TEST_UID_2)
        self.assertNotEqual(node_id, node_id2)

    def test_eq_not_equal_different_class(self) -> None:
        node_id = BlankNodeId(TEST_UID)
        node_id2 = object()
        self.assertNotEqual(node_id, node_id2)

    def test_repr(self) -> None:
        node_id = BlankNodeId(TEST_UID)
        self.assertEqual(repr(node_id), TEST_REPR)

    def test_to_nquad_statement(self) -> None:
        node_id = BlankNodeId(TEST_UID)
        self.assertEqual(node_id.to_nquad_statement(), TEST_NQUAD_STATEMENT)
