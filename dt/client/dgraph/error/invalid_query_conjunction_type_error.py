from dt.client.dgraph.error.dgraph_error import DGraphError


class InvalidQueryConjunctionTypeError(DGraphError):
    ''' Referenced a nonexistent query conjunction type '''
