from typing import Set
from dt.dgraph.dql.scalar_predicate import ScalarPredicate


class Node:
    scalar_predicates: Set[ScalarPredicate]
    uid: str

    ''' Represents a single DGraph Node.
    
    Attributes:
        uid: The node's unique id
        scalar_predicates: A set of scalar predicates for the given node.
    '''

    def __init__(self, uid: str):
        self.uid = uid
        self.scalar_predicates = set()

    def add_scalar_predicate(self, predicate: ScalarPredicate) -> ScalarPredicate:
        '''Adds a scalar predicate to the given node

        Args:
            predicate: the predicate to add

        Returns:
            The added predicate
        '''
        self.scalar_predicates.add(predicate)
        return predicate

    def __hash__(self) -> int:
        return hash((self.uid, self.scalar_predicates))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.uid == other.uid and \
            self.scalar_predicates == other.scalar_predicates

    def __repr__(self) -> str:
        return f"Node({self.uid})"
