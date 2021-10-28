from unittest import TestCase
from mre import Regex


class TestRegex(TestCase):
    def setUp(self):
        self.regex = Regex("[A-z]")

    def test_eq(self):
        self.assertTrue(self.regex == "[A-z]")

    def test_iadd(self):
        self.regex += "{3}"
        self.assertTrue(self.regex == "[A-z]{3}")

    def test_set(self):
        self.regex._set_regex("[0-9]{5}")
        self.assertTrue(self.regex == "[0-9]{5}")

    def test_add(self):
        self.regex = Regex("[0-9]{5}") + "-" + Regex("[0-9]{3}")
        self.assertTrue(self.regex == "[0-9]{5}-[0-9]{3}")
