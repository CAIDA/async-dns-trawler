from dt.client.dgraph.error.dgraph_error import DGraphError


class MutationError(DGraphError):
    ''' Error occured when attempting to mutate Dgraph database '''
