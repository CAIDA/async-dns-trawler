from dt.dgraph.dql.node_id import NodeId


class BlankNodeId(NodeId):
    '''Represents a node id for a blank node that is convertable to an
    RDF N-Quad term

    Attributes
        value: The id to store
    '''

    value: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BlankNodeId):
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def to_nquad_statement(self) -> str:
        return f"_:{self.value}"
