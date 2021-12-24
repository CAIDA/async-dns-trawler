from dt.client.dgraph.dql.node_predicate import NodePredicate
from dt.client.dgraph.dql.triple import Triple
from dt.client.dgraph.dql.triple_set import TripleSet
from dt.client.dgraph.entity.i_entity import IEntity
from dt.client.dgraph.entity.node import Node


class Link(IEntity):
    ''' Represents an edge between two DGraph nodes

    Attributes:
        link_type: the relationship between the two nodes
        source: The source node
        target: The target node
    '''

    def __init__(self, link_type: str, source: Node, target: Node):
        self.link_type = link_type
        self.source = source
        self.target = target

    def __hash__(self) -> int:
        return hash((self.link_type, self.source, self.target))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Link):
            return False
        return self.link_type == other.link_type and \
            self.source == other.source and \
            self.target == other.target

    def __repr__(self) -> str:
        return f"Link({self.link_type}, source={self.source.uid}, target={self.target.uid})"

    def to_dql_triples(self) -> TripleSet:
        node_predicate = NodePredicate(self.link_type, self.target.uid)
        triple = Triple(self.source.uid, node_predicate)
        triples_set = TripleSet({triple})
        return triples_set
