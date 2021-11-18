from abc import ABCMeta, abstractmethod
from typing import Set

from dt.dgraph.dql.triple import Triple


class IEntity:
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_dql_triples(self) -> Set[Triple]:
        raise NotImplementedError
