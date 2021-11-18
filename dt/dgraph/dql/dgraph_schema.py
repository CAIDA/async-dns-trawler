from typing import List, Set, Optional

from dt.dgraph.dql.i_schema_item import ISchemaItem
from dt.dgraph.dql.node_schema import NodeSchema
from dt.dgraph.dql.type_attribute import TypeAttribute
from dt.dgraph.error.schema_duplicate_error import SchemaDuplicateError


class DGraphSchema(ISchemaItem):
    '''Defines a schema for an entire DGraph Database'''

    _node_schema_list: List[NodeSchema]
    _node_schema_type_set: Set[str]

    def __init__(self, node_schema_list: Optional[List[NodeSchema]] = None):
        self._node_schema_list = []
        self._node_schema_type_set = set()
        if node_schema_list is not None:
            for node_schema in node_schema_list:
                self.add_node_schema(node_schema)

    def add_node_schema(self, node_schema: NodeSchema) -> NodeSchema:
        if node_schema.node_type in self._node_schema_type_set:
            message = f"Node with type: {node_schema.node_type} already " + \
                "exists in current DGraph schema"
            raise SchemaDuplicateError(message)
        self._node_schema_type_set.add(node_schema.node_type)
        self._node_schema_list.append(node_schema)
        return node_schema

    def get_attributes(self) -> List[TypeAttribute]:
        combined_type_attributes = {}
        for node_schema in self._node_schema_list:
            for type_attribute in node_schema.get_attributes():
                attr_name = type_attribute.attr_name
                if attr_name not in combined_type_attributes:
                    combined_type_attributes[attr_name] = type_attribute
                elif combined_type_attributes[attr_name] != type_attribute:
                    message = f"Attribute with name: {attr_name} from node_type: " + \
                    f"{node_schema.node_type} conflicts with current DGraph schema"
                    raise SchemaDuplicateError(message)

        return sorted(combined_type_attributes.values())

    def to_schema_statement(self) -> str:
        attribute_schema_list = [attr.to_schema_statement() for attr in self.get_attributes()]
        attr_schema_list_str = "\n".join(attribute_schema_list)
        node_type_schema_list = [node_schema.to_schema_statement() for node_schema in self._node_schema_list]
        node_type_schema_list_str = "\n".join(node_type_schema_list)
        db_schema_str = "\n".join([attr_schema_list_str, node_type_schema_list_str])
        return db_schema_str
