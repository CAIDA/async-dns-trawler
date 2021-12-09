from dt.dns_trawler.error.dns_trawler_error import DNSTrawlerError


class InvalidQueryError(DNSTrawlerError):
    ''' DB query uses incorrect types '''
