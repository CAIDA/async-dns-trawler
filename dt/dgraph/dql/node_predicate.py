from dt.dgraph.entity.node import Node


class NodePredicate:
    ''' Defines a single DGraph node predicate pertaining to a link
    between nodes.

    Attributes:
        predicate_name: The name of the relationship between nodes.
        predicate_value: The target node for the relationship
    '''

    predicate_name: str
    predicate_value: Node

    def __init__(self, predicate_name: str, predicate_value: Node):
        self.predicate_name = predicate_name
        self.predicate_value = predicate_value

    def __hash__(self) -> int:
        return hash((self.predicate_name, self.predicate_value.uid))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NodePredicate):
            return False
        return self.predicate_name == other.predicate_name and \
            self.predicate_value == other.predicate_value

    def __repr__(self) -> str:
        return f"NodePredicate({self.predicate_name}, {self.predicate_value})"
