from typing import Any

from dt.dns_trawler.constants.sort_direction import SortDirection
from dt.dns_trawler.db.query_field import QueryField


class OrderBy:
    def __init__(self, query_field: QueryField, sort_direction: SortDirection):
        self.query_field = query_field
        self.sort_direction = sort_direction

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, OrderBy):
            return False
        return self.query_field == other.query_field and \
            self.sort_direction == other.sort_direction

    def __repr__(self) -> str:
        return f"OrderBy({self.query_field.field_name}, {self.sort_direction.name})"
