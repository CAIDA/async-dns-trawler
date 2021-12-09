import unittest

from dt.dgraph.constants.rdf_type import RDFType
from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.error.invalid_scalar_type_error import InvalidScalarTypeError
from dt.dgraph.mapper.scalar_type_mapper import ScalarTypeMapper


class ScalarTypeMapperTestCase(unittest.TestCase):
    def test_to_rdf_type_successful(self) -> None:
        expected = RDFType.INT
        actual = ScalarTypeMapper.to_rdf_type(ScalarType.INT)
        self.assertEqual(actual, expected)

    def test_from_rdf_type_successful(self) -> None:
        expected = ScalarType.STRING
        actual = ScalarTypeMapper.from_rdf_type(RDFType.STRING)
        self.assertEqual(actual, expected)

    def test_to_schema_attribute_type_successful(self) -> None:
        expected = SchemaAttributeType.STRING
        actual = ScalarTypeMapper.to_schema_attribute_type(ScalarType.STRING)
        self.assertEqual(actual, expected)

    def test_from_schema_attribute_type_successful(self) -> None:
        expected = ScalarType.STRING
        actual = ScalarTypeMapper.from_schema_attribute_type(SchemaAttributeType.STRING)
        self.assertEqual(actual, expected)

    def test_from_schema_attribute_type_error_uid(self) -> None:
        def uid_conversion() -> None:
            ScalarTypeMapper.from_schema_attribute_type(SchemaAttributeType.UID)
        self.assertRaises(InvalidScalarTypeError, uid_conversion)

    def test_from_schema_attribute_type_error_default(self) -> None:
        def default_conversion() -> None:
            ScalarTypeMapper.from_schema_attribute_type(SchemaAttributeType.DEFAULT)
        self.assertRaises(InvalidScalarTypeError, default_conversion)
