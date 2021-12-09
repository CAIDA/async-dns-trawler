from typing import Tuple, Union

from dt.dgraph.constants.query_conjunction_type import QueryConjunctionType
from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable
from dt.dgraph.graphql.query_function import QueryFunction


class QueryConjunction(IGraphQLSerializable):

    def __init__(self, conjunction_type: QueryConjunctionType, args: Tuple[Union[QueryFunction, "QueryConjunction"]]):
        self.conjunction_type = conjunction_type
        self.args = args

    def to_graphql(self) -> str:
        graphql_str_list = [el.to_graphql() for el in self.args]
        conjunction = f" {self.conjunction_type.name} "
        conjoined_str = conjunction.join(graphql_str_list)
        graphql_str = f"({conjoined_str})"
        return graphql_str
