from typing import Any, Tuple

from dt.dns_trawler.constants.query_operator import QueryOperator
from dt.dns_trawler.error.invalid_query_error import InvalidQueryError


class QueryExpression:
    def __init__(self, query_operator: QueryOperator, args: Tuple[Any, ...]):
        self.query_operator = query_operator
        self.args = args

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, QueryExpression):
            return False
        return self.query_operator == other.query_operator and \
            self.args == other.args

    def __repr__(self) -> str:
        args_str = ", ".join(map(repr, self.args))
        return f"{self.query_operator.name}({args_str})"

    def __and__(self, other: object) -> 'QueryExpression':
        if not isinstance(other, QueryExpression):
            message = "Compared values should be of type QueryExpression"
            raise InvalidQueryError(message)
        return QueryExpression(QueryOperator.AND, (self, other))

    def __or__(self, other: object) -> 'QueryExpression':
        if not isinstance(other, QueryExpression):
            message = "Compared values should be of type QueryExpression"
            raise InvalidQueryError(message)
        return QueryExpression(QueryOperator.OR, (self, other))

    def __invert__(self) -> 'QueryExpression':
        return QueryExpression(QueryOperator.NOT, (self,))
