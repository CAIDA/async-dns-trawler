from dt.dgraph.constants.rdf_type import RDFType
from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.constants.schema_attribute_type import SchemaAttributeType
from dt.dgraph.error.invalid_scalar_type_error import InvalidScalarTypeError


class ScalarTypeMapper:
    @staticmethod
    def to_rdf_type(scalarType: ScalarType) -> RDFType:
        return RDFType[scalarType.name]

    @staticmethod
    def from_rdf_type(rdfType: RDFType) -> ScalarType:
        return ScalarType[rdfType.name]

    @staticmethod
    def to_schema_attribute_type(scalarType: ScalarType) -> SchemaAttributeType:
        return SchemaAttributeType[scalarType.name]

    @staticmethod
    def from_schema_attribute_type(schemaAttributeType: SchemaAttributeType) -> ScalarType:
        if schemaAttributeType is SchemaAttributeType.UID or \
           schemaAttributeType is SchemaAttributeType.DEFAULT:
            raise InvalidScalarTypeError

        return ScalarType[schemaAttributeType.name]
