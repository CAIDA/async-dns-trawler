from abc import ABCMeta, abstractmethod


class IRDFConvertable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_nquad_statement(self) -> str:
        raise NotImplementedError
