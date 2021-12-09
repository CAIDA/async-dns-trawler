from typing import Optional

from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable
from dt.util.separated_by import newline_separated, single_space_separated


class BlockScope(IGraphQLSerializable):
    ''' Represents a named block scope

    Attributes:
        block_type: Type of code block
        label: Label for the code block
        parameters: Content of parameters if function block
        body: The terms inside the block
    '''

    def __init__(self, block_type: Optional[str] = None,
                 label: Optional[str] = None,
                 parameters: Optional[str] = None,
                 body: Optional[str] = None):
        self.block_type = block_type
        self.label = label
        self.parameters = parameters
        self.body = body

    def to_graphql(self) -> str:
        label = ""
        if self.label is not None:
            label = self.label
        if self.parameters is not None:
            label = f"{label}({self.parameters})"
        heading_parts = list(filter(None, [self.block_type, label]))
        rows = []
        if self.body is not None:
            heading_parts.append("{")
            rows.extend([self.body, "}"])
        heading = single_space_separated(heading_parts)
        rows.insert(0, heading)
        graphql_str = newline_separated(rows)
        return graphql_str
