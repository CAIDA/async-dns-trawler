from dt.client.dgraph.error.dgraph_error import DGraphError


class PredicateValueError(DGraphError):
    ''' The value assigned to a predicate is unsupported '''
