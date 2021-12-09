from typing import Any, Tuple

from dt.dgraph.constants.comparison_function import ComparisonFunction
from dt.dgraph.graphql.block_scope import BlockScope
from dt.dgraph.graphql.graphql import GraphQL
from dt.dgraph.graphql.value import Value
from dt.typing.custom_types.input_value import InputValue
from dt.util.separated_by import comma_separated


class QueryFunction(Value):
    def __init__(self, comp_func: ComparisonFunction, args: Tuple[InputValue, ...]):
        self.comp_func = comp_func
        self.args = args

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, QueryFunction):
            return False
        return self.comp_func == other.comp_func and \
            self.args == other.args

    def __hash__(self) -> int:
        return hash((self.comp_func, self.args))

    def to_graphql(self) -> str:
        label = str(self.comp_func.value)
        parameters = comma_separated(GraphQL(self.args))
        block_scope = BlockScope(label=label, parameters=parameters)
        return GraphQL(block_scope)
