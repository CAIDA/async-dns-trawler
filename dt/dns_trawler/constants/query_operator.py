from enum import Enum


class QueryOperator(Enum):
    EQ = "eq"
    NE = "ne"
    LT = "lt"
    LE = "le"
    GT = "gt"
    GE = "ge"
    AND = "and"
    OR = "or"
    NOT = "not"
