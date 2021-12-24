from typing import Tuple

from dt.client.dgraph.constants.query_conjunction_type import \
    QueryConjunctionType
from dt.client.dgraph.dql.query_function import QueryFunction
from dt.client.dgraph.graphql.graphql import GraphQL
from dt.client.dgraph.graphql.value import Value


class QueryConjunction(QueryFunction):
    def __init__(self, comp_func: QueryConjunctionType, args: Tuple[Value, ...]):
        self.comp_func = comp_func
        self.args = args

    def to_graphql(self) -> str:
        if self.comp_func == QueryConjunctionType.NOT:
            conjunction_str = f"{self.comp_func.value} {GraphQL(self.args[0])}"
        else:
            conjunction = f' {self.comp_func.value} '
            conjunction_str = conjunction.join(GraphQL(self.args))
        graphql_str = f"({conjunction_str})"
        return graphql_str
