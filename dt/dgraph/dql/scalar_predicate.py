from typing import Any

from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.dql.predicate import Predicate
from dt.dgraph.dql.node_schema import NodeSchema
from dt.dgraph.mapper.scalar_type_mapper import ScalarTypeMapper


class ScalarPredicate(Predicate):
    ''' Defines a single DGraph node predicate with it's corresponding
    object value for scalar type.

    Attributes:
        predicate_type: The DGraph type for the predicate
    '''

    predicate_type: ScalarType

    def __init__(self, predicate_name: str, predicate_value: Any, predicate_type: ScalarType):
        super().__init__(predicate_name, predicate_value)
        self.predicate_type = predicate_type

    def __hash__(self) -> int:
        return hash((self.predicate_name, self.predicate_type, self.predicate_value))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ScalarPredicate):
            return False
        return self.predicate_name == other.predicate_name and \
            self.predicate_type == other.predicate_type and \
            self.predicate_value == other.predicate_value

    def __repr__(self) -> str:
        return f"ScalarPredicate({self.predicate_name}, {self.predicate_value}, {self.predicate_type})"

    def to_nquad_statement(self) -> str:
        '''Returns a formatted string containing the predicate, datatype,
        and object of an RDF N-Quad statement'''
        rdf_type = ScalarTypeMapper.to_rdf_type(self.predicate_type)
        return f'<{self.predicate_name}> "{self.predicate_value}"^^{rdf_type.value}'
