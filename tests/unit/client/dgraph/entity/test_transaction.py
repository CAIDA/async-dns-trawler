import unittest

from dt.client.dgraph.dql.node_id import NodeId
from dt.client.dgraph.dql.predicate import Predicate
from dt.client.dgraph.dql.triple import Triple
from dt.client.dgraph.entity.node import Node
from dt.client.dgraph.entity.transaction import Transaction

TEST_NODE_ID = "0x1"
TEST_NODE_ID_2 = "0x2"
TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_PREDICATE_VALUE = "TEST_PREDICATE_VALUE"


class TransactionTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        node = Node(TEST_NODE_ID)
        transaction = Transaction({node})
        self.assertEqual(transaction.entities, {node})

    def test_to_dql_triples(self) -> None:
        node_id = NodeId(TEST_NODE_ID)
        node_id2 = NodeId(TEST_NODE_ID_2)
        node = Node(TEST_NODE_ID)
        node2 = Node(TEST_NODE_ID_2)
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_PREDICATE_VALUE)
        node.add_predicate(predicate)
        node2.add_predicate(predicate)
        transaction = Transaction({node, node2})
        self.assertEqual(transaction.to_dql_triples(), {
            Triple(node_id, predicate),
            Triple(node_id2, predicate),
        })
