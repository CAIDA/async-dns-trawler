from dt.dns_trawler.error.dns_trawler_error import DNSTrawlerError


class ResourceAlreadyExistsError(DNSTrawlerError):
    ''' Error thrown when a response is returned for a given query when
        the referenced element should not exist'''
