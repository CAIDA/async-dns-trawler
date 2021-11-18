from typing import Any

from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.dql.type_attribute import TypeAttribute
from dt.dgraph.dql.node_predicate import NodePredicate
from dt.dgraph.dql.predicate import Predicate
from dt.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.dgraph.mapper.scalar_type_mapper import ScalarTypeMapper

class AttributePredicateMapper:
    @staticmethod
    def to_predicate(type_attribute:TypeAttribute, value:Any) -> Predicate:
        attr_name = type_attribute.attr_name
        attr_type = type_attribute.attr_type
        if attr_type == SchemaAttributeType.UID:
            predicate = NodePredicate(attr_name, value)
        elif attr_type == SchemaAttributeType.DEFAULT:
            predicate = Predicate(attr_name, value)
        else:
            predicate_type = ScalarTypeMapper.from_schema_attribute_type(attr_type)
            predicate = ScalarPredicate(attr_name, value, predicate_type)
        return predicate