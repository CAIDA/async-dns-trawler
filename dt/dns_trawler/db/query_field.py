from typing import Any

from dt.dns_trawler.constants.query_operator import QueryOperator
from dt.dns_trawler.db.query_expression import QueryExpression
from dt.dns_trawler.error.invalid_query_error import InvalidQueryError
from dt.util.is_primitive import is_primitive


class QueryField:

    def __init__(self, field_name: str):
        self.field_name = field_name

    def __repr__(self) -> str:
        return f"QueryField({self.field_name})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, QueryField):
            return False
        return self.field_name == other.field_name

    def eq(self, other: Any) -> QueryExpression:
        if not is_primitive(other):
            message = "Compared values should be of type int, float, str, or bool"
            raise InvalidQueryError(message)
        return QueryExpression(QueryOperator.EQ, (self, other))

    def ne(self, other: Any) -> QueryExpression:
        if not is_primitive(other):
            message = "Compared values should be of type int, float, str, or bool"
            raise InvalidQueryError(message)
        return QueryExpression(QueryOperator.NE, (self, other))

    def lt(self, other: Any) -> QueryExpression:
        if not is_primitive(other):
            message = "Compared values should be of type int, float, str, or bool"
            raise InvalidQueryError(message)
        return QueryExpression(QueryOperator.LT, (self, other))

    def le(self, other: Any) -> QueryExpression:
        if not is_primitive(other):
            message = "Compared values should be of type int, float, str, or bool"
            raise InvalidQueryError(message)
        return QueryExpression(QueryOperator.LE, (self, other))

    def gt(self, other: Any) -> QueryExpression:
        if not is_primitive(other):
            message = "Compared values should be of type int, float, str, or bool"
            raise InvalidQueryError(message)
        return QueryExpression(QueryOperator.GT, (self, other))

    def ge(self, other: Any) -> QueryExpression:
        if not is_primitive(other):
            message = "Compared values should be of type int, float, str, or bool"
            raise InvalidQueryError(message)
        return QueryExpression(QueryOperator.GE, (self, other))
