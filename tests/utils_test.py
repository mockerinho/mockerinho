import unittest

from mockerinho import utils


class UtilsTestCase(unittest.TestCase):
    def test_should_get_version_number(self):
        expected = '1.0.0'
        actual = utils.get_version_number((1, 0, 0))
        self.assertEqual(expected, actual)
