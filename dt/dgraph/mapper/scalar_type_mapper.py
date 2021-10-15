from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.constants.rdf_type import RDFType


class ScalarTypeMapper:
    @staticmethod
    def to_rdf_type(scalarType: ScalarType) -> RDFType:

        # DGraph default and string scalar types both use the underlying
        # Go string type. https://dgraph.io/docs/query-language/schema/
        if scalarType is ScalarType.DEFAULT:
            return RDFType.STRING

        return RDFType[scalarType.name]

    @staticmethod
    def from_rdf_type(rdfType: RDFType) -> ScalarType:
        return ScalarType[rdfType.name]
