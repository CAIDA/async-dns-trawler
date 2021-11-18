from dt.dgraph.dql.i_rdf_convertable import IRDFConvertable


class NodeId(IRDFConvertable):
    '''Represents a node id that is convertable to an RDF N-Quad term

    Attributes
        value: The id to store
    '''

    value: str

    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NodeId):
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def to_nquad_statement(self) -> str:
        return f"<{self.value}>"

    def __repr__(self) -> str:
        return self.value
