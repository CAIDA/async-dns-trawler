import unittest

from dt.client.dgraph.dql.blank_node_id import BlankNodeId
from dt.client.dgraph.entity.blank_node import BlankNode

TEST_UID = "TEST_UID"


class BlankNodeTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        node = BlankNode(TEST_UID)
        self.assertIsInstance(node.uid, BlankNodeId)
