from unittest import TestCase
from mre import Regex, Quantifier, Anchor


class TestAnchor(TestCase):
    def setUp(self):
        self.regex = Regex(Quantifier(Regex.DIGIT, 4), '-', Quantifier(Regex.WORD_CHARS, 1, without_maximum=True), '.txt')

    def test_anchor(self):
        rgx_anchor = Anchor(self.regex)
        self.assertTrue(rgx_anchor == "^\\d{4}-\\w+.txt$")

    def test_anchor_negative(self):
        rgx_anchor = Anchor(self.regex, negate=True)
        self.assertTrue(rgx_anchor == "\\b\\d{4}-\\w+.txt\\B")
