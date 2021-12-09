from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.predicate import Predicate


class NodePredicate(Predicate):
    ''' Defines a single DGraph node predicate pertaining to a link
    between nodes.

    Attributes:
        predicate_name: The name of the relationship between nodes.
        predicate_value: The target node's id for the relationship
    '''

    def __init__(self, predicate_name: str, predicate_value: NodeId):
        predicate_value_str = predicate_value.to_nquad_statement()
        super().__init__(predicate_name, predicate_value_str)

    def __hash__(self) -> int:
        return hash((self.predicate_name, self.predicate_value))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NodePredicate):
            return False
        return self.predicate_name == other.predicate_name and \
            self.predicate_value == other.predicate_value

    def __repr__(self) -> str:
        return f"NodePredicate({self.predicate_name}, {self.predicate_value})"

    def to_nquad_statement(self) -> str:
        '''Returns a formatted string containing the predicate
        and object of an RDF N-Quad statement'''
        return f'<{self.predicate_name}> {self.predicate_value}'
