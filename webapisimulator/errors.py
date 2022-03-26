
class WebApiSimulatorError(Exception):
    pass


class MatcherError(WebApiSimulatorError):
    pass


class ExactMatcherError(MatcherError):
    pass


class RegexpMatcherError(MatcherError):
    pass


class JsonMatcherError(MatcherError):
    pass
