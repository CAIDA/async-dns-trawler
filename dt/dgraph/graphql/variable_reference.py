from typing import Any

from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable


class VariableReference(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL variable
     based on http://spec.graphql.org/June2018/#Variable
    '''

    def __init__(self, variable_name: str):
        self.variable_name = variable_name

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, VariableReference):
            return False
        return self.variable_name == other.variable_name

    def __hash__(self) -> int:
        return hash(self.variable_name)

    def to_graphql(self) -> str:
        return f"${self.variable_name}"
