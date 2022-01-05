from unittest import TestCase

from mre import Regex, RegexBase


class TestRegex(TestCase):
    def test_init(self):
        regex = RegexBase(Regex('[A-z]'))
        self.assertTrue(regex == '[A-z]')

    def test_iadd(self):
        regex = Regex('[A-z]')
        regex += '{3}'
        self.assertTrue(regex == '[A-z]{3}')

    def test_add(self):
        regex = RegexBase('[0-9]{5}') + '-' + RegexBase('[0-9]{3}')
        self.assertTrue(regex == '[0-9]{5}-[0-9]{3}')
