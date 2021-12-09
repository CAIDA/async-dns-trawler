from typing import Set

from dt.dgraph.dql.i_rdf_convertable import IRDFConvertable
from dt.dgraph.dql.triple import Triple
from dt.util.separated_by import newline_separated


class TripleSet(Set[Triple], IRDFConvertable):
    ''' Represents a collection of DQL triples '''

    def to_nquad_statement(self) -> str:
        nquad_list = sorted([triple.to_nquad_statement() for triple in self])
        nquad_str = newline_separated(nquad_list)
        return nquad_str
