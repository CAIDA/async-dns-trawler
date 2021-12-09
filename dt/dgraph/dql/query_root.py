from typing import Optional, Set

from dt.dgraph.dql.query_function import QueryFunction
from dt.dgraph.graphql.argument import Argument
from dt.dgraph.graphql.value import Value

_QUERY_ROOT_ARG_NAME = "func"
_FIRST_ARG_NAME = "first"
_OFFSET_ARG_NAME = "offset"
_AFTER_ARG_NAME = "after"


class QueryRoot:
    def __init__(self, func: QueryFunction,
                 first: Optional[int] = None,
                 offset: Optional[int] = None,
                 after: Optional[int] = None):
        self.func = func
        self.first = first
        self.offset = offset
        self.after = after

    def to_argument_set(self) -> Set[Argument]:
        argument_set = set()
        argument_set.add(Argument(_QUERY_ROOT_ARG_NAME, self.func))
        if self.first is not None:
            argument_set.add(Argument(_FIRST_ARG_NAME, Value(self.first)))
        if self.offset is not None:
            argument_set.add(Argument(_OFFSET_ARG_NAME, Value(self.offset)))
        if self.after is not None:
            argument_set.add(Argument(_AFTER_ARG_NAME, Value(self.after)))
        return argument_set
