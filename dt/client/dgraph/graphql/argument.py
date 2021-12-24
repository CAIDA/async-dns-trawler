from typing import Any

from dt.client.dgraph.graphql.graphql import GraphQL
from dt.client.dgraph.graphql.i_graphql_serializable import \
    IGraphQLSerializable
from dt.typing.custom_types.input_value import InputValue


class Argument(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL argument based on
    http://spec.graphql.org/June2018/#sec-Language.Arguments
    '''

    def __init__(self, name: str, input_value: InputValue):
        self.name = name
        self.input_value = input_value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Argument):
            return False
        return self.name == other.name and \
            self.input_value == other.input_value

    def __hash__(self) -> int:
        return hash((self.name, self.input_value))

    def to_graphql(self) -> str:
        graphql_str = f"{self.name}: {GraphQL(self.input_value)}"
        return graphql_str
