from abc import ABCMeta, abstractmethod
from typing import Generic, TypeVar

from dt.dns_trawler.db.query_options import QueryOptions
from dt.dns_trawler.db.query_response import QueryResponse

T = TypeVar('T')

# Note: All raised errors come from dt.dns_trawler.error


class IDatabaseClient(Generic[T]):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, item: T) -> T:
        ''' Retrieves a full item given a sparse key item
        Args:
            item: Sparse key item
        Returns:
            The retrieved resource
        Raises:
            ResourceNotFoundError if the requested resource does not
                exist in the database
            InternalServerError: if the query fails
        '''

    @abstractmethod
    def create(self, item: T) -> T:
        ''' Create an item in the database
        Args:
            item: The resource to create
        Returns:
            The created resource
        Raises:
            ResourceAlreadyExistsError if the requested resource already
                exists in the database
            InternalServerError: if the mutation fails
        '''

    @abstractmethod
    def update(self, item: T) -> T:
        ''' Update an item in the database
        Args:
            item: The resource to update
        Returns:
            The updated resource
        Raises:
            ResourceNotFoundError if the resource to update does not
                exist in the database
            InternalServerError: if the mutation fails
        '''

    @abstractmethod
    def delete(self, item: T) -> None:
        ''' Delete an item from the database
        Args:
            item: The resource to delete
        Raises:
            InternalServerError: if the mutation fails
        '''

    @abstractmethod
    def query(self, query_options: QueryOptions) -> QueryResponse[T]:
        ''' Retrieve a list of items from the database that match a
            certain query
        Args:
            query_options: Config for the query
        Returns:
            A list items of matching the query
        Raises:
            InternalServerError: if the query fails
        '''
