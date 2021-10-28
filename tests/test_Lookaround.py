from unittest import TestCase
from mre import Regex, Lookahead


class TestGroup(TestCase):
    def setUp(self):
        self.regex = Regex("[A-z]")

    def test_positive_lookahead(self):
        lookahead = self.regex + Lookahead("water")
        self.assertTrue(lookahead == "[A-z](?=water)")

    def test_negative_lookahead(self):
        lookahead = self.regex + Lookahead("water", must_not_include=True)
        self.assertTrue(lookahead == "[A-z](?!water)")

    def test_positive_lookahead_regex(self):
        lookahead = self.regex + Lookahead(Regex('Test'))
        self.assertTrue(lookahead == "[A-z](?=Test)")

    def test_positive_lookahead_backreference(self):
        lookahead = self.regex + Lookahead(1)
        self.assertTrue(lookahead == "[A-z](?=\\1)")
