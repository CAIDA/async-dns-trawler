import unittest

from dt.dgraph.dql.predicate import Predicate
from dt.dgraph.entity.node import Node

TEST_UID = "0x1"


class NodeTestCase(unittest.TestCase):

    def test_constructor(self) -> None:
        node = Node(TEST_UID)
        self.assertEqual(node.scalar_predicates, set())

    # def test_add_predicate(self):
    #     node = Node()
    #     self.assertEqual(len(node.predicates), 0)
    #     predicate = Predicate()
    #     node.add_predicate(predicate)
    #     self.assertEqual(len(node.predicates), 1)
