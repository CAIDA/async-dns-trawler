from abc import ABCMeta, abstractmethod


class IRDFConvertable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_nquad_statement(self) -> str:
        ''' Returns a string containing a partial or whole RDF N-Quad statement '''
