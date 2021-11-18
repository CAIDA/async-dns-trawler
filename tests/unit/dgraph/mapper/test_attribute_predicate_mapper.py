import unittest

from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.mapper.attribute_predicate_mapper import AttributePredicateMapper
from dt.dgraph.dql.type_attribute import TypeAttribute
from dt.dgraph.dql.blank_node_id import BlankNodeId
from dt.dgraph.dql.node_predicate import NodePredicate
from dt.dgraph.dql.predicate import Predicate
from dt.dgraph.dql.scalar_predicate import ScalarPredicate

TEST_PREDICATE_NAME = "TEST_PREDICATE_NAME"
TEST_SCALAR_TYPE = ScalarType.STRING
TEST_SCHEMA_TYPE_1 = SchemaAttributeType.STRING
TEST_SCHEMA_TYPE_2 = SchemaAttributeType.UID
TEST_SCHEMA_TYPE_3 = SchemaAttributeType.DEFAULT
TEST_PREDICATE_VALUE = "TEST_PREDICATE_VALUE"
TEST_UID = "TEST_UID"

class AttributePredicateMapperTestCase(unittest.TestCase):
    def test_to_predicate_scalar_predicate(self) -> None:
        expected = ScalarPredicate(TEST_PREDICATE_NAME, TEST_PREDICATE_VALUE, TEST_SCALAR_TYPE)
        type_attribute = TypeAttribute(TEST_PREDICATE_NAME, TEST_SCHEMA_TYPE_1)
        actual = AttributePredicateMapper.to_predicate(type_attribute, TEST_PREDICATE_VALUE)
        self.assertEqual(actual, expected)

    def test_to_predicate_node_predicate(self) -> None:
        node_id = BlankNodeId(TEST_UID)
        expected = NodePredicate(TEST_PREDICATE_NAME, node_id)
        type_attribute = TypeAttribute(TEST_PREDICATE_NAME, TEST_SCHEMA_TYPE_2)
        actual = AttributePredicateMapper.to_predicate(type_attribute, node_id)
        self.assertEqual(actual, expected)

    def test_to_predicate_predicate(self) -> None:
        expected = Predicate(TEST_PREDICATE_NAME, TEST_PREDICATE_VALUE)
        type_attribute = TypeAttribute(TEST_PREDICATE_NAME, TEST_SCHEMA_TYPE_3)
        actual = AttributePredicateMapper.to_predicate(type_attribute, TEST_PREDICATE_VALUE)
        self.assertEqual(actual, expected)