import json
import re
import typing as t

from . import errors


class ExactMatcher:
    def __init__(self, suitable: str) -> None:
        if not isinstance(suitable, str):
            raise errors.ExactMatcherError(
                'The "suitable" must be a string.'
            )

        self.__suitable_string = suitable

    def matches(self, captured: str) -> bool:
        return self.__suitable_string == captured


class RegexpMatcher:
    def __init__(self, suitable: str) -> None:
        if not isinstance(suitable, str):
            raise errors.RegexpMatcherError(
                'The "suitable" must be a string.'
            )

        try:
            suitable_regexp = re.compile(suitable)
        except re.error:
            raise errors.RegexpMatcherError(
                'The "suitable" must be a valid regexp pattern.'
            )

        self.__suitable_regexp = suitable_regexp

    def matches(self, captured: str) -> bool:
        return bool(self.__suitable_regexp.match(captured))


class JsonMatcher:
    def __init__(self, suitable: str) -> None:
        if not isinstance(suitable, str):
            raise errors.JsonMatcherError(
                'The "suitable" must be a string.'
            )

        suitable_json = JsonMatcher.__try_json_loads(suitable)

        if suitable_json is None:
            raise errors.JsonMatcherError(
                'The "suitable" must be a valid json string.'
            )

        self.__suitable_json = suitable_json

    def matches(self, captured: str) -> bool:
        captured_json = JsonMatcher.__try_json_loads(captured)

        if captured_json is None:
            return False

        captured_contains_suitable = self.__suitable_json.items() <= captured_json.items()

        return captured_contains_suitable

    @staticmethod
    def __try_json_loads(s: str) -> t.Optional[dict]:
        try:
            loaded = json.loads(s)
        except json.JSONDecodeError:
            loaded = None

        return loaded
