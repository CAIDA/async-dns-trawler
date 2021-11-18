''' Contains the different index variants for scalar predicates.
(https://dgraph.io/docs/query-language/schema/)'''

from enum import Enum


class PredicateIndex(Enum):
    pass


class StringIndex(PredicateIndex):
    HASH = "hash"
    EXACT = "exact"
    TERM = "term"
    FULLTEXT = "fulltext"
    TRIGRAM = "trigram"


class DateTimeIndex(PredicateIndex):
    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    HOUR = "hour"


class IntIndex(PredicateIndex):
    INT = "int"


class FloatIndex(PredicateIndex):
    FLOAT = "float"


class BoolIndex(PredicateIndex):
    BOOL = "bool"


class GeoIndex(PredicateIndex):
    GEO = "geo"
