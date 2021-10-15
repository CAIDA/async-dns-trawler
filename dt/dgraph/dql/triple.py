from dt.dgraph.dql.predicate import Predicate


class Triple:
    '''Represents a DGraph mutation triple. In handling mutations,
    DGraph expects triples in RDF N-Quad format https://www.w3.org/TR/n-quads/.

    '''

    subject: str
    predicate: Predicate
