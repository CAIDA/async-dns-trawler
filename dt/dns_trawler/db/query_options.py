from typing import Optional

from dt.dns_trawler.db.order_by import OrderBy
from dt.dns_trawler.db.query_expression import QueryExpression


class QueryOptions:
    ''' A config for database query

    Attributes:
        expression: Query expression to filter against
        max_results: Maximum number of records to return
        next_token: Pagination token for where to begin next query
        order_by: The field to sort by and the direction to sort
                        in for the query results.
    '''

    def __init__(self, expression: QueryExpression,
                 max_results: Optional[int] = None,
                 next_token: Optional[str] = None,
                 order_by: Optional[OrderBy] = None):
        self.expression = expression
        self.max_results = max_results
        self.next_token = next_token
        self.order_by = order_by

    def __repr__(self) -> str:
        repr_terms = [f"expression={self.expression}"]
        if self.max_results is not None:
            repr_terms.append(f"max_results={self.max_results}")
        if self.next_token is not None:
            repr_terms.append(f"next_token={self.next_token}")
        if self.order_by is not None:
            repr_terms.append(f"order_by={self.order_by}")
        repr_terms_str = ", ".join(repr_terms)
        repr_str = f"QueryOptions({repr_terms_str})"
        return repr_str
