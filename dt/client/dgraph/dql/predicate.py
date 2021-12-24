from typing import Any

from dt.client.dgraph.dql.i_rdf_convertable import IRDFConvertable


class Predicate(IRDFConvertable):
    ''' Defines a single DGraph node predicate with it's corresponding
    object value.

    Attributes:
        predicate_name: The name for the node's data attribute
        predicate_value: The string representation of the predicate's
                         corresponding value
    '''

    predicate_name: str
    predicate_value: str

    def __init__(self, predicate_name: str, predicate_value: Any):
        self.predicate_name = predicate_name
        self.predicate_value = str(predicate_value)

    def __hash__(self) -> int:
        return hash((self.predicate_name, self.predicate_value))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Predicate):
            return False
        return self.predicate_name == other.predicate_name and \
            self.predicate_value == other.predicate_value

    def __repr__(self) -> str:
        return f"Predicate({self.predicate_name}, {self.predicate_value})"

    def to_nquad_statement(self) -> str:
        '''Returns a formatted string containing the predicate and object
        of an RDF N-Quad statement'''
        return f'<{self.predicate_name}> "{self.predicate_value}"'
