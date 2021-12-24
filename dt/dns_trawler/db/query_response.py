from typing import Any, Generic, List, Optional, TypeVar

T = TypeVar('T')


class QueryResponse(Generic[T]):
    def __init__(self, items: List[T], next_token: Optional[str] = None):
        self.items = items
        self.next_token = next_token

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, QueryResponse):
            return False
        return self.items == other.items and \
            self.next_token == other.next_token
