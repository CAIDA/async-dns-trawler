from typing import Any

from dt.client.dgraph.graphql.i_graphql_serializable import \
    IGraphQLSerializable


class FragmentSpread(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL fragment spread based on
    http://spec.graphql.org/June2018/#FragmentSpread
    '''

    def __init__(self, fragment_name: str):
        self.fragment_name = fragment_name

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, FragmentSpread):
            return False
        return self.fragment_name == other.fragment_name

    def __hash__(self) -> int:
        return hash(self.fragment_name)

    def to_graphql(self) -> str:
        spread_operator = "..."
        graphql_str = f"{spread_operator}{self.fragment_name}"
        return graphql_str
