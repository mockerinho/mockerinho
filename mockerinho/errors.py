

class Error(Exception):
    pass


class MatcherError(Error):
    pass


class IncorrectSuitableError(MatcherError):
    pass
