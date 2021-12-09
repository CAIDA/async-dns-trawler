from enum import Enum


class QueryConjunction(Enum):
    AND = "and"
    OR = "or"
    NOT = "not"
