from typing import Tuple

from dt.dgraph.constants.comparison_function import ComparisonFunction
from dt.dgraph.graphql.block_scope import BlockScope
from dt.dgraph.graphql.graphql import GraphQL
from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable


class QueryFunction(IGraphQLSerializable):

    def __init__(self, cmp_func: ComparisonFunction, args: Tuple[str]):
        block_type = cmp_func.value
        parameters = ", ".join(args)
        self.block_scope = BlockScope(block_type=block_type,
                                      parameters=parameters)

    def to_graphql(self) -> str:
        return GraphQL(self.block_scope)
