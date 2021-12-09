from abc import ABCMeta, abstractmethod

from dt.dgraph.dql.triple_set import TripleSet


class IEntity:
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_dql_triples(self) -> TripleSet:
        ''' Returns a set of triples representing the entity's predicates '''
