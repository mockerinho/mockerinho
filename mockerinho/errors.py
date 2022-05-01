
class MockerinhoError(Exception):
    """A base class for errors used by mockerinho."""
    pass


class MatcherError(MockerinhoError):
    """This is a base class for all errors related
    to request matchers."""


class IncorrectSuitableError(MatcherError):
    pass
