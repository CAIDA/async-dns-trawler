from dt.client.dgraph.error.dgraph_error import DGraphError


class InvalidQueryExpressionError(DGraphError):
    ''' QueryExpression contains an unsupported operator or invalid syntax  '''
