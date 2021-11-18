from dt.dgraph.error.dgraph_error import DGraphError


class InvalidScalarTypeError(DGraphError):
    ''' Referenced a nonexistent scalar type '''
