from dt.client.dgraph.error.dgraph_error import DGraphError


class InvalidComparisonFunctionError(DGraphError):
    ''' Referenced a nonexistent comparison function '''
