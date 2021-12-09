from enum import Enum
from typing import Any

from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable
from dt.typing.custom_types.value_literal import ValueLiteral


class Value(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL non-variable value
    based on http://spec.graphql.org/June2018/#sec-Input-Values
    '''

    def __init__(self, value: ValueLiteral):
        self.value = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Value):
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def to_graphql(self) -> str:
        if isinstance(self.value, Enum):
            return str(self.value.value)
        return str(self.value)
