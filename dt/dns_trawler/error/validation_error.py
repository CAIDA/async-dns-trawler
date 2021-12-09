from dt.dns_trawler.error.dns_trawler_error import DNSTrawlerError


class ValidationError(DNSTrawlerError):
    ''' Error thrown when there is an invalid request or response'''
