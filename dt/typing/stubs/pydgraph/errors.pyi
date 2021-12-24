from typing import Any

from pydgraph.meta import VERSION as VERSION

__maintainer__: str
__status__: str

class AbortedError(Exception):
    def __init__(self) -> None: ...

class RetriableError(Exception):
    exception: Any
    def __init__(self, exception:Any) -> None: ...

class ConnectionError(Exception):
    exception: Any
    def __init__(self, exception:Any) -> None: ...

class TransactionError(Exception):
    def __init__(self, msg:str) -> None: ...
