from dt.client.dgraph.constants.comparison_function import ComparisonFunction
from dt.client.dgraph.error.invalid_comparison_function_error import \
    InvalidComparisonFunctionError
from dt.dns_trawler.constants.query_operator import QueryOperator


class ComparisonFunctionMapper:
    @staticmethod
    def is_comparison_function(query_operator: QueryOperator) -> bool:
        return query_operator.name in ComparisonFunction.__members__

    @staticmethod
    def from_query_operator(query_operator: QueryOperator) -> ComparisonFunction:
        if not ComparisonFunctionMapper.is_comparison_function(query_operator):
            message = f"{query_operator.name} is not a valid comparisonFunction"
            raise InvalidComparisonFunctionError(message)

        return ComparisonFunction[query_operator.name]
