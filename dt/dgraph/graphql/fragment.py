from typing import Any

from dt.dgraph.graphql.block_scope import BlockScope
from dt.dgraph.graphql.fragment_spread import FragmentSpread
from dt.dgraph.graphql.graphql import GraphQL
from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable
from dt.dgraph.graphql.selection_set import SelectionSet


class Fragment(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL fragment based on
    http://spec.graphql.org/June2018/#sec-Language.Fragments
    '''

    def __init__(self, name: str, type_condition: str, selection_set: SelectionSet):
        self.name = name
        self.type_condition = type_condition
        self.selection_set = selection_set

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Fragment):
            return False
        return self.name == other.name and \
            self.type_condition == other.type_condition and \
            self.selection_set == other.selection_set

    def __hash__(self) -> int:
        return hash((self.name, self.type_condition, self.selection_set))

    def fragment_spread(self) -> FragmentSpread:
        fragment_spread = FragmentSpread(self.name)
        return fragment_spread

    def to_graphql(self) -> str:
        label = f"fragment {self.name} on {self.type_condition}"
        body = GraphQL(self.selection_set)
        block_scope = BlockScope(label=label, body=body)
        return GraphQL(block_scope)
