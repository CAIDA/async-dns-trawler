from abc import ABCMeta, abstractmethod


class ISchemaItem:
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_schema_statement(self) -> str:
        ''' Returns a string containing a partial or whole DGraph Schema '''
