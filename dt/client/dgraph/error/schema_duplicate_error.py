from dt.client.dgraph.error.dgraph_error import DGraphError


class SchemaDuplicateError(DGraphError):
    ''' Schema element is referenced more than once within a single
    schema context '''
