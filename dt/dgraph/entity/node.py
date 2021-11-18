from typing import Set
from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.predicate import Predicate
from dt.dgraph.dql.triple import Triple
from dt.dgraph.entity.i_entity import IEntity


class Node(IEntity):
    predicates: Set[Predicate]
    uid: NodeId

    ''' Represents a single DGraph Node.

    Attributes:
        uid: The node's unique id
        predicates: A set of predicates for the given node.
    '''

    def __init__(self, uid: str):
        self.uid = NodeId(uid)
        self.predicates = set()

    def add_predicate(self, predicate: Predicate) -> Predicate:
        '''Adds a predicate to the given node

        Args:
            predicate: the predicate to add

        Returns:
            The added predicate
        '''
        self.predicates.add(predicate)
        return predicate

    def __hash__(self) -> int:
        return hash((self.uid, tuple(self.predicates)))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.uid == other.uid and \
               self.predicates == other.predicates

    def __repr__(self) -> str:
        return f"Node({self.uid})"

    def to_dql_triples(self) -> Set[Triple]:
        triples_set = set()
        for predicate in self.predicates:
            triple = Triple(self.uid, predicate)
            triples_set.add(triple)
        return triples_set
