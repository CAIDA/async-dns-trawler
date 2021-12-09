from ipaddress import IPv4Address, IPv6Address
from typing import Any, Union


class Host:
    ''' Represents a single DNS host with a name and IP address '''

    def __init__(self, name: str, address: Union[IPv4Address, IPv6Address]):
        self.name = name
        self.address = IPv6Address

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Host):
            return False
        return self.name == other.name and \
            self.address == other.address

    def __hash__(self) -> int:
        return hash((self.name, self.address))
