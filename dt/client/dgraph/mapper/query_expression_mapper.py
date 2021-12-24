from dt.client.dgraph.dql.query_conjunction import QueryConjunction
from dt.client.dgraph.dql.query_function import QueryFunction
from dt.client.dgraph.error.invalid_query_expression_error import \
    InvalidQueryExpressionError
from dt.client.dgraph.graphql.value import Value
from dt.client.dgraph.mapper.comparison_function_mapper import \
    ComparisonFunctionMapper
from dt.client.dgraph.mapper.query_conjunction_type_mapper import \
    QueryConjunctionTypeMapper
from dt.dns_trawler.constants.query_operator import QueryOperator
from dt.dns_trawler.db.query_expression import QueryExpression
from dt.dns_trawler.db.query_field import QueryField


class QueryExpressionMapper:
    @staticmethod
    def to_query_function(expression: QueryExpression) -> QueryFunction:
        operator = expression.query_operator
        if operator == QueryOperator.NE:
            new_expression = ~QueryExpression(QueryOperator.EQ, expression.args)
            return QueryExpressionMapper.to_query_function(new_expression)

        parsed_args = []
        for arg in expression.args:
            if isinstance(arg, QueryField):
                parsed = Value(arg.field_name)
            elif isinstance(arg, QueryExpression):
                parsed = QueryExpressionMapper.to_query_function(arg)
            else:
                parsed = Value(arg)
            parsed_args.append(parsed)
        tuple_parsed_args = tuple(parsed_args)

        if QueryConjunctionTypeMapper.is_query_conjunction_type(operator):
            conjunction_type = QueryConjunctionTypeMapper.from_query_operator(operator)
            query_conjunction = QueryConjunction(conjunction_type, tuple_parsed_args)
            return query_conjunction
        elif ComparisonFunctionMapper.is_comparison_function(operator):
            comparison_function = ComparisonFunctionMapper.from_query_operator(operator)
            query_function = QueryFunction(comparison_function, tuple_parsed_args)
            return query_function
        else:
            message = f"QueryOperator {operator} can not be converted to a query function"
            raise InvalidQueryExpressionError(message)
