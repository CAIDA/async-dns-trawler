from typing import Optional

from dt.dns_trawler.constants.sort_direction import SortDirection
from dt.dns_trawler.db.query_expression import QueryExpression


class QueryOptions:
    ''' A config for database query

    Attributes:
        expression: Query expression to filter against
        max_results: Maximum number of records to return
        next_token: Pagination token for where to begin next query
        sort_direction: Whether results should be sorted ascending or
                        descending
    '''

    def __init__(self, expression: QueryExpression,
                 max_results: Optional[int] = None,
                 next_token: Optional[str] = None,
                 sort_direction: Optional[SortDirection] = None):
        self.expression = expression
        self.max_results = max_results
        self.next_token = next_token
        self.sort_direction = sort_direction

    def __repr__(self) -> str:
        repr_terms = [f"expression={self.expression}"]
        if self.max_results is not None:
            repr_terms.append(f"max_results={self.max_results}")
        if self.next_token is not None:
            repr_terms.append(f"next_token={self.next_token}")
        if self.sort_direction is not None:
            repr_terms.append(f"sort_direction={self.sort_direction.name}")
        repr_terms_str = ", ".join(repr_terms)
        repr_str = f"QueryOptions({repr_terms_str})"
        return repr_str
