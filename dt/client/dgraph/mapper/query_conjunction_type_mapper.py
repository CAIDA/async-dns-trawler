from dt.client.dgraph.constants.query_conjunction_type import \
    QueryConjunctionType
from dt.client.dgraph.error.invalid_query_conjunction_type_error import \
    InvalidQueryConjunctionTypeError
from dt.dns_trawler.constants.query_operator import QueryOperator


class QueryConjunctionTypeMapper:
    @staticmethod
    def is_query_conjunction_type(query_operator: QueryOperator) -> bool:
        return query_operator.name in QueryConjunctionType.__members__

    @staticmethod
    def from_query_operator(query_operator: QueryOperator) -> QueryConjunctionType:
        if not QueryConjunctionTypeMapper.is_query_conjunction_type(query_operator):
            message = f"{query_operator.name} is not a valid query conjunction type"
            raise InvalidQueryConjunctionTypeError(message)

        return QueryConjunctionType[query_operator.name]
