from typing import Any, Iterable, Union

from dt.dgraph.graphql.fragment import Fragment
from dt.dgraph.graphql.graphql import GraphQL
from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable
from dt.dgraph.graphql.operation import Operation
from dt.util.separated_by import newline_separated


class Document(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL document based on
    http://spec.graphql.org/June2018/#sec-Language.Document
    '''

    def __init__(self, definitions: Iterable[Union[Operation, Fragment]]):
        self.definitions = list(definitions)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Document):
            return False
        return self.definitions == other.definitions

    def __hash__(self) -> int:
        return hash(frozenset(self.definitions))

    def to_graphql(self) -> str:
        graphql_str_list = GraphQL(self.definitions)
        graphql_str = newline_separated(graphql_str_list)
        return graphql_str
