from typing import Set

from dt.client.dgraph.dql.triple_set import TripleSet
from dt.client.dgraph.entity.i_entity import IEntity


class Transaction(IEntity):
    ''' Represents a collection of database entities that can be used
    in a single mutation

    Attributes:
        entities: Collection of entities for mutation
    '''

    def __init__(self, entities: Set[IEntity]):
        self.entities = entities

    def to_dql_triples(self) -> TripleSet:
        combined_triples = TripleSet()
        for entity in self.entities:
            triples = entity.to_dql_triples()
            combined_triples.update(triples)
        return combined_triples
