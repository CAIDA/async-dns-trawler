from abc import ABCMeta, abstractmethod


class ISchemaItem:
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_schema_statement(self) -> str:
        raise NotImplementedError
