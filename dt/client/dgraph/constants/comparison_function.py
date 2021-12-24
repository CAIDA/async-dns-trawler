from enum import Enum


class ComparisonFunction(Enum):
    EQ = "eq"
    LT = "lt"
    LE = "le"
    GT = "gt"
    GE = "ge"
    ALL_OF_TERMS = "allOfTerms"
    ANY_OF_TERMS = "anyOfTerms"
    UID = "uid"
    UID_IN = "uid_in"
    HAS = "has"
    NEAR = "near"
    WITHIN = "within"
    CONTAINS = "contains"
    INTERSECTS = "intersects"
