from functools import total_ordering
from typing import Iterable, Optional, Set

from dt.client.dgraph.constants.index_type import PredicateIndex
from dt.client.dgraph.constants.schema_attribute_type import \
    SchemaAttributeType
from dt.client.dgraph.dql.i_schema_item import ISchemaItem
from dt.util.separated_by import comma_separated, single_space_separated


@total_ordering
class TypeAttribute(ISchemaItem):
    '''Defines a single DGraph Schema predicate

    Attributes:
        attr_name: The attribute's name
        attr_type: The attribute's datatype
        is_list_type: Flag to indicate if attribute supports multiple values
        indices: Set of indexes to put on the attribute'''

    attr_name: str
    attr_type: SchemaAttributeType
    is_list_type: bool
    indices: Set[PredicateIndex]

    def __init__(self, attr_name: str, attr_type: SchemaAttributeType,
                 is_list_type: bool = False, indices: Optional[Iterable[PredicateIndex]] = None):
        self.attr_name = attr_name
        self.attr_type = attr_type
        self.is_list_type = is_list_type

        if indices is None:
            indices = set()
        self.indices = set(indices)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TypeAttribute):
            return False
        return self.attr_name == other.attr_name and \
            self.attr_type == other.attr_type and \
            self.is_list_type == other.is_list_type and \
            self.indices == other.indices

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, TypeAttribute):
            return NotImplemented
        return self.attr_name < other.attr_name

    def to_schema_statement(self) -> str:
        attribute_terms = []

        if self.is_list_type:
            type_term = f"[{self.attr_type.value}]"
        else:
            type_term = self.attr_type.value
        attribute_terms.append(type_term)

        if len(self.indices) > 0:
            index_name_list = sorted([index.value for index in self.indices])
            index_name_str = comma_separated(index_name_list)
            index_term = f"@index({index_name_str})"
            attribute_terms.append(index_term)

        term_str = single_space_separated(attribute_terms)
        return f"{self.attr_name}: {term_str} ."
