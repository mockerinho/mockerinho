import unittest

from webapisimulator import errors, matchers


class ExactMatcherTest(unittest.TestCase):
    def test_should_raise_regexp_matcher_error_if_suitable_is_not_a_string(self):
        for unsuitable in [777, None, str]:
            with self.assertRaises(errors.ExactMatcherError):
                _ = matchers.ExactMatcher(unsuitable)

    def test_should_match_string_which_equals_to_suitable_string(self):
        suitable = 'suitable'
        matcher = matchers.ExactMatcher(suitable)
        captured = 'suitable'
        self.assertTrue(matcher.matches(captured))

    def test_should_not_match_string_which_differs_from_suitable_string(self):
        suitable = 'suitable'
        matcher = matchers.ExactMatcher(suitable)
        captured = 'captured'
        self.assertFalse(matcher.matches(captured))


class RegexpMatcherTest(unittest.TestCase):
    def test_should_raise_regexp_matcher_error_if_suitable_is_not_a_string(self):
        for unsuitable in [777, None, str]:
            with self.assertRaises(errors.RegexpMatcherError):
                _ = matchers.RegexpMatcher(unsuitable)

    def test_should_match_string_which_matches_suitable_regexp_pattern(self):
        suitable = '^a*b*c*$'
        matcher = matchers.RegexpMatcher(suitable)
        for captured in ['', 'a', 'b', 'c', 'ab', 'ac', 'bc']:
            self.assertTrue(matcher.matches(captured))

    def test_should_not_match_string_which_does_not_match_suitable_regexp_pattern(self):
        suitable = '^a{3}$'
        matcher = matchers.RegexpMatcher(suitable)
        for captured in ['', 'a', 'aa', 'aaaa']:
            self.assertFalse(matcher.matches(captured))


class JsonMatcherTest(unittest.TestCase):
    def test_should_raise_json_matcher_error_if_suitable_is_not_a_string(self):
        for unsuitable in [777, None, str]:
            with self.assertRaises(errors.JsonMatcherError):
                _ = matchers.JsonMatcher(unsuitable)

    def test_should_raise_json_matcher_error_if_suitable_is_not_a_valid_json_string(self):
        suitable = 'This string is not suitable tho...'
        with self.assertRaises(errors.JsonMatcherError):
            _ = matchers.JsonMatcher(suitable)

    def test_should_match_json_string_which_equals_to_suitable_json_string(self):
        suitable = '{"name":"Mike", "surname": "Wazowski"}'
        matcher = matchers.JsonMatcher(suitable)
        captured = '{"surname": "Wazowski", "name":"Mike"}'
        self.assertTrue(matcher.matches(captured))

    def test_should_not_match_string_which_is_not_a_valid_json_string(self):
        suitable = '{"name":"Mike", "surname": "Wazowski"}'
        matcher = matchers.JsonMatcher(suitable)
        captured = 'Not a JSON string'
        self.assertFalse(matcher.matches(captured))

    def test_should_match_string_which_has_nested_json(self):
        suitable = '{"name": "Mike", "surname": "Wazowski", "passport": {"number": "7777", "series": "777"}}'
        matcher = matchers.JsonMatcher(suitable)
        captured = '{"surname": "Wazowski", "name": "Mike", "passport": {"series": "777", "number": "7777"}}'
        self.assertTrue(matcher.matches(captured))
