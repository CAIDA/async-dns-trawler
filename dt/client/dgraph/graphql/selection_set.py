from typing import Any, Union

from dt.client.dgraph.graphql.field import Field
from dt.client.dgraph.graphql.fragment_spread import FragmentSpread
from dt.client.dgraph.graphql.graphql import GraphQL
from dt.client.dgraph.graphql.i_graphql_serializable import \
    IGraphQLSerializable
from dt.util.separated_by import newline_separated


class SelectionSet(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL selection set
    based on http://spec.graphql.org/June2018/#SelectionSet
    '''

    def __init__(self, *args: Union[Field, FragmentSpread]):
        self.items = set(args)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SelectionSet):
            return False
        return self.items == other.items

    def __hash__(self) -> int:
        return hash(frozenset(self.items))

    def to_graphql(self) -> str:
        selection_set_str_list = sorted(GraphQL(self.items))
        graphql_str = newline_separated(selection_set_str_list)
        return graphql_str
