from abc import ABCMeta, abstractmethod


class IGraphQLSerializable:
    __metaclass__ = ABCMeta

    def __repr__(self) -> str:
        classname = type(self).__name__
        return f"{classname}[{self.to_graphql()}]"

    @abstractmethod
    def to_graphql(self) -> str:
        ''' Returns a string containing a partial or whole GraphQL operation '''
