import unittest

from dt.dgraph.client.transaction import Transaction
from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.predicate import Predicate
from dt.dgraph.entity.node import Node

TEST_NODE_ID = "0x1"
TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_PREDICATE_VALUE = "TEST_PREDICATE_VALUE"
TEST_NQUAD_STATEMENT = '<0x1> <TEST_PREDICATE_NAME> "TEST_PREDICATE_VALUE" .'


class TransactionTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        node_id = NodeId(TEST_NODE_ID)
        node = Node(node_id)
        transaction = Transaction({node})
        self.assertEqual(transaction.entities, {node})

    def test_to_nquad_statement(self) -> None:
        node_id = NodeId(TEST_NODE_ID)
        node = Node(node_id)
        predicate = Predicate(TEST_PREDICATE_NAME, TEST_PREDICATE_VALUE)
        node.add_predicate(predicate)
        transaction = Transaction({node})
        self.assertEqual(transaction.to_nquad_statement(), TEST_NQUAD_STATEMENT)