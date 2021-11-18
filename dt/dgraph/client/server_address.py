from typing import Optional

class ServerAddress:
    ''' Represents the socket address for a DGraph database node 
    
    Attributes:
        host: the node's hostname
        port: the target port
    '''

    def __init__(self, host:str, port:Optional[int] = None):
        self.host = host
        self.port = port

    def __hash__(self) -> int:
        return hash((self.host, self.port))

    def __eq__(self, other:object) -> bool:
        if not isinstance(other, ServerAddress):
            return False
        return self.host == other.host and \
               self.port == other.port

    def __repr__(self) -> str:
        return f"ServerAddress({self.get_address()})"

    def get_address(self) -> str:
        if self.port is None:
            return self.host
        return f"{self.host}:{self.port}"