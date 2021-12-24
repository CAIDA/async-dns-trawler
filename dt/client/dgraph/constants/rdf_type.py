from enum import Enum


class RDFType(Enum):
    # Subset of DGraph's supported RDF datatypes
    # for 1:1 map between DGraph type to RDF datatype
    # (https://dgraph.io/docs/mutations/language-rdf-types/)

    INT = "<xs:int>"
    FLOAT = "<xs:float>"
    STRING = "<xs:string>"
    BOOL = "<xs:boolean>"
    DATETIME = "<xs:dateTime>"
    GEO = "<geo:geojson>"
    PASSWORD = "<xs:password>"
