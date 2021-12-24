from typing import Optional, Set

from dt.client.dgraph.dql.query_function import QueryFunction
from dt.client.dgraph.graphql.argument import Argument
from dt.client.dgraph.graphql.value import Value

_QUERY_ROOT_ARG_NAME = "func"
_FIRST_ARG_NAME = "first"
_OFFSET_ARG_NAME = "offset"
_AFTER_ARG_NAME = "after"
_ORDERASC_ARG_NAME = "orderasc"
_ORDERDESC_ARG_NAME = "orderdesc"


class QueryRoot:
    def __init__(self, func: QueryFunction,
                 first: Optional[int] = None,
                 offset: Optional[int] = None,
                 after: Optional[str] = None,
                 orderasc: Optional[str] = None,
                 orderdesc: Optional[str] = None,
                 ):
        self.func = func
        self.first = first
        self.offset = offset
        self.after = after
        self.orderasc = orderasc
        self.orderdesc = orderdesc

    def to_argument_set(self) -> Set[Argument]:
        argument_set = set()
        argument_set.add(Argument(_QUERY_ROOT_ARG_NAME, self.func))
        if self.first is not None:
            argument_set.add(Argument(_FIRST_ARG_NAME, Value(self.first)))
        if self.offset is not None:
            argument_set.add(Argument(_OFFSET_ARG_NAME, Value(self.offset)))
        if self.after is not None:
            argument_set.add(Argument(_AFTER_ARG_NAME, Value(self.after)))
        if self.orderasc is not None:
            argument_set.add(Argument(_ORDERASC_ARG_NAME, Value(self.orderasc)))
        if self.orderdesc is not None:
            argument_set.add(Argument(_ORDERDESC_ARG_NAME, Value(self.orderdesc)))
        return argument_set
