from typing import Set

from dt.dgraph.dql.i_rdf_convertable import IRDFConvertable
from dt.dgraph.entity.i_entity import IEntity

class Transaction(IRDFConvertable):
    ''' Represents a collection of database entities that can be used
    in a single mutation

    Attributes:
        entities: Collection of entities for mutation
    '''

    def __init__(self, entities:Set[IEntity]):
        self.entities = entities

    def to_nquad_statement(self) -> str:
        transaction_nquad_set = set()
        for entity in self.entities:
            triples = entity.to_dql_triples()
            nquad_triples = {triple.to_nquad_statement() for triple in triples}
            transaction_nquad_set.update(nquad_triples)
        transaction_nquad_str = "\n".join(transaction_nquad_set)
        return transaction_nquad_str

