from abc import ABCMeta, abstractmethod


class IDNSClient:
    __metaclass__ = ABCMeta

    @abstractmethod
    def query(self, query):
        ''' Retrieves a full item given a sparse key item '''
