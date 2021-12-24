from abc import ABCMeta, abstractmethod

from dt.dns_trawler.dns.dns_query import DNSQuery
from dt.dns_trawler.dns.dns_response import DNSResponse


class IDNSClient:
    __metaclass__ = ABCMeta

    @abstractmethod
    def query(self, query: DNSQuery) -> DNSResponse:
        ''' Retrieves a full item given a sparse key item '''
