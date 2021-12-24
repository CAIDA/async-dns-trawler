from enum import Enum


class SchemaAttributeType(Enum):
    ''' Valid datatype for schema attributes. Encompasses all scalar
    attribute types, as well as a default type and a uid type for
    node predicates'''

    DEFAULT = "default"
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    DATETIME = "dateTime"
    GEO = "geo"
    PASSWORD = "password"
    UID = "uid"
