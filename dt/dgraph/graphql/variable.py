from typing import Any, Optional

from dt.dgraph.graphql.graphql import GraphQL
from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable
from dt.dgraph.graphql.value import Value
from dt.dgraph.graphql.variable_reference import VariableReference


class Variable(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL variable definition
    based on http://spec.graphql.org/June2018/#VariableDefinition
    '''

    def __init__(self, name: str,
                 variable_type: str,
                 value: Optional[Value] = None,
                 default_value: Optional[Value] = None):
        self.name = name
        self.variable_type = variable_type
        self.value = value
        self.default_value = default_value

    def get_reference(self) -> VariableReference:
        return VariableReference(self.name)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Variable):
            return False
        return self.name == other.name and \
            self.variable_type == other.variable_type and \
            self.value == other.value and \
            self.default_value == other.default_value

    def __hash__(self) -> int:
        return hash((self.name,
                     self.variable_type,
                     self.value,
                     self.default_value))

    def to_graphql(self) -> str:
        reference = self.get_reference()
        graphql_str = f"{GraphQL(reference)}: {self.variable_type}"
        if self.default_value is not None:
            graphql_str += " = " + GraphQL(self.default_value)
        return graphql_str
