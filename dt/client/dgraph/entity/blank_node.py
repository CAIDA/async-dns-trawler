from dt.client.dgraph.dql.blank_node_id import BlankNodeId
from dt.client.dgraph.entity.node import Node


class BlankNode(Node):

    ''' Represents a single DGraph Node nonexistent in the database.

    Attributes:
        uid: The node's temporary unique id
    '''

    def __init__(self, uid: str):
        super().__init__(uid)
        self.uid = BlankNodeId(uid)
