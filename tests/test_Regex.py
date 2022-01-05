from unittest import TestCase

from mre import Regex


class TestRegex(TestCase):
    def test_eq(self):
        self.assertTrue(Regex('[A-z]') == '[A-z]')

    def test_iadd(self):
        regex = Regex('[A-z]')
        regex += '{3}'
        self.assertTrue(regex == '[A-z]{3}')

    def test_set(self):
        regex = Regex('[A-z]')
        regex._set_regex('[0-9]{5}')
        self.assertTrue(regex == '[0-9]{5}')

    def test_add(self):
        regex = Regex('[0-9]{5}') + '-' + Regex('[0-9]{3}')
        self.assertTrue(regex == '[0-9]{5}-[0-9]{3}')

    def test_str(self):
        regex = Regex('[A-z]')
        string_print = regex.__str__()
        self.assertTrue(string_print == '[A-z]')
