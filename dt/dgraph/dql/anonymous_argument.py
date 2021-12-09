from typing import Any

from dt.dgraph.graphql.argument import Argument
from dt.dgraph.graphql.graphql import GraphQL
from dt.typing.custom_types.input_value import InputValue


class AnonymousArgument(Argument):
    def __init__(self, input_value: InputValue):
        self.input_value = input_value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AnonymousArgument):
            return False
        return self.input_value == other.input_value

    def __hash__(self) -> int:
        return hash(self.input_value)

    def to_graphql(self) -> str:
        graphql_str = GraphQL(self.input_value)
        return graphql_str
