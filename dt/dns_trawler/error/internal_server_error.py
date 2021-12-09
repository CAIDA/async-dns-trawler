from dt.dns_trawler.error.dns_trawler_error import DNSTrawlerError


class InternalServerError(DNSTrawlerError):
    ''' Error thrown when PyDgraph transaction fails '''
