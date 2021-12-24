from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Set

from dt.client.dgraph.graphql.argument import Argument
from dt.client.dgraph.graphql.block_scope import BlockScope
from dt.client.dgraph.graphql.graphql import GraphQL
from dt.client.dgraph.graphql.i_graphql_serializable import \
    IGraphQLSerializable
from dt.util.separated_by import comma_separated

if TYPE_CHECKING:
    from dt.client.dgraph.graphql.selection_set import SelectionSet


class Field(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL field based on
    http://spec.graphql.org/June2018/#sec-Language.Fields

    Attributes:
        name: The field name
        alias: A different name under which the value will be returned
        parameters: Content of parameters if function block
        body: The terms inside the block
    '''

    def __init__(self, name: str,
                 alias: Optional[str] = None,
                 arguments: Optional[Set[Argument]] = None,
                 selection_set: Optional[SelectionSet] = None):
        self.name = name
        self.alias = alias
        self.arguments = arguments
        self.selection_set = selection_set

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Field):
            return False
        return self.name == other.name and \
            self.alias == other.alias and \
            self.arguments == other.arguments and \
            self.selection_set == other.selection_set

    def __hash__(self) -> int:
        arguments = None
        if self.arguments is not None:
            arguments = tuple(self.arguments)
        return hash((self.name, self.alias, arguments, self.selection_set))

    def to_graphql(self) -> str:
        label = self.name
        parameters = None
        body = None
        if self.alias is not None:
            label = f"{self.alias}: {label}"
        if self.arguments is not None:
            argument_str_list = sorted(GraphQL(self.arguments))
            parameters = comma_separated(argument_str_list)
        if self.selection_set is not None:
            body = GraphQL(self.selection_set)
        block_scope = BlockScope(label=label,
                                 parameters=parameters,
                                 body=body)
        return GraphQL(block_scope)
