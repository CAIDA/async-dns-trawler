from enum import Enum


class ScalarType(Enum):
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    DATETIME = "dateTime"
    GEO = "geo"
    PASSWORD = "password"
