from typing import Any

from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.dql.node_id import NodeId
from dt.dgraph.dql.node_predicate import NodePredicate
from dt.dgraph.dql.predicate import Predicate
from dt.dgraph.dql.scalar_predicate import ScalarPredicate
from dt.dgraph.dql.type_attribute import TypeAttribute
from dt.dgraph.error.predicate_value_error import PredicateValueError
from dt.dgraph.mapper.scalar_type_mapper import ScalarTypeMapper


class AttributePredicateMapper:
    @staticmethod
    def to_predicate(type_attribute: TypeAttribute, value: Any) -> Predicate:
        attr_name = type_attribute.attr_name
        attr_type = type_attribute.attr_type
        if attr_type == SchemaAttributeType.UID:
            if isinstance(value, NodeId):
                node_id = value
            elif isinstance(value, str):
                node_id = NodeId(value)
            else:
                message = f"Expected value: {value} to be of type str or NodeId"
                raise PredicateValueError(message)
            return NodePredicate(attr_name, node_id)
        elif attr_type == SchemaAttributeType.DEFAULT:
            return Predicate(attr_name, value)
        else:
            predicate_type = ScalarTypeMapper.from_schema_attribute_type(attr_type)
            return ScalarPredicate(attr_name, value, predicate_type)
