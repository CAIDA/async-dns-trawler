from typing import Optional

from dt.dgraph.constants.graphql_operation import GraphQLOperation
from dt.dgraph.dql.query_root import QueryRoot
from dt.dgraph.graphql.field import Field
from dt.dgraph.graphql.operation import Operation
from dt.dgraph.graphql.selection_set import SelectionSet
from dt.dgraph.graphql.variable_set import VariableSet


class QueryOperation(Operation):
    def __init__(self,
                 name: str,
                 selection_set: SelectionSet,
                 query_root: QueryRoot,
                 variables: Optional[VariableSet] = None):
        query_field_arguments = query_root.to_argument_set()
        query_field = Field(name=name,
                            arguments=query_field_arguments,
                            selection_set=selection_set)
        operation_selection_set = SelectionSet(query_field)
        super().__init__(operation_type=GraphQLOperation.QUERY,
                         selection_set=operation_selection_set,
                         name=name,
                         variables=variables)
