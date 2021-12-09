from typing import Any, Optional

from dt.dgraph.constants.graphql_operation import GraphQLOperation
from dt.dgraph.graphql.block_scope import BlockScope
from dt.dgraph.graphql.graphql import GraphQL
from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable
from dt.dgraph.graphql.selection_set import SelectionSet
from dt.dgraph.graphql.variable_set import VariableSet


class Operation(IGraphQLSerializable):
    ''' Class representing a simplified GraphQL document based on
    http://spec.graphql.org/June2018/#sec-Language.Operations
    '''

    def __init__(self, operation_type: GraphQLOperation,
                 selection_set: SelectionSet,
                 name: Optional[str] = None,
                 variables: Optional[VariableSet] = None):
        self.operation_type = operation_type
        self.name = name
        self.selection_set = selection_set
        self.variables = variables

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Operation):
            return False
        return self.operation_type == other.operation_type and \
            self.name == other.name and \
            self.selection_set == other.selection_set and \
            self.variables == other.variables

    def __hash__(self) -> int:
        return hash((
            self.operation_type,
            self.name,
            self.selection_set,
            self.variables
        ))

    def to_graphql(self) -> str:
        block_type = self.operation_type.value
        label = self.name
        parameters = None
        if self.variables is not None:
            parameters = GraphQL(self.variables)
        body = GraphQL(self.selection_set)
        block_scope = BlockScope(block_type=block_type,
                                 label=label,
                                 parameters=parameters,
                                 body=body)
        graphql_str = GraphQL(block_scope)
        return graphql_str
