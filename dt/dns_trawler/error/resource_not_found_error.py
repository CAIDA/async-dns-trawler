from dt.dns_trawler.error.dns_trawler_error import DNSTrawlerError


class ResourceNotFoundError(DNSTrawlerError):
    ''' Error thrown when no response is returned for a given query or
        a referenced element does not exist'''
