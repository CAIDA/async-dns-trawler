from enum import Enum


class ScalarType(Enum):
    DEFAULT = "default"
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    DATETIME = "dateTime"
    GEO = "geo"
    PASSWORD = "password"
