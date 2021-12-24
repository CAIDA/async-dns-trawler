from dt.client.dgraph.dql.i_rdf_convertable import IRDFConvertable
from dt.client.dgraph.dql.node_id import NodeId
from dt.client.dgraph.dql.predicate import Predicate


class Triple(IRDFConvertable):
    '''Represents a DGraph mutation triple. In handling mutations,
    DGraph expects triples in RDF N-Quad format https://www.w3.org/TR/n-quads/.

    Attributes:
        subject: The id for the DGraph node for which the predicate is applicable
        predicate: The predicate to apply to the node
    '''

    subject: NodeId
    predicate: Predicate

    def __init__(self, subject: NodeId, predicate: Predicate):
        self.subject = subject
        self.predicate = predicate

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Triple):
            return False
        return self.subject == other.subject and \
            self.predicate == other.predicate

    def __hash__(self) -> int:
        return hash((self.subject, self.predicate))

    def to_nquad_statement(self) -> str:
        return f"{self.subject.to_nquad_statement()} {self.predicate.to_nquad_statement()} ."
