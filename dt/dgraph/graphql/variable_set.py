from typing import Any

from dt.dgraph.graphql.graphql import GraphQL
from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable
from dt.dgraph.graphql.variable import Variable
from dt.util.separated_by import comma_separated


class VariableSet(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL variable definition list
    based on https://spec.graphql.org/June2018/#VariableDefinition
    '''

    def __init__(self, *args: Variable):
        self.items = set(args)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, VariableSet):
            return False
        return self.items == other.items

    def __hash__(self) -> int:
        return hash(frozenset(self.items))

    def to_graphql(self) -> str:
        variable_str_list = sorted(GraphQL(self.items))
        graphql_str = comma_separated(variable_str_list)
        return graphql_str
