from unittest import TestCase

from mre import Anchor, Comment, Quantifier, Regex


class TestAnchor(TestCase):
    def setUp(self):
        chars = Quantifier(Regex.WORD_CHARS, 1, without_maximum=True)
        self.regex = Regex(Quantifier(Regex.DIGIT, 4), '-', chars, '.txt')

    def test_anchor(self):
        rgx_anchor = Anchor(self.regex)
        self.assertTrue(rgx_anchor == '^\\d{4}-\\w+.txt$')

    def test_anchor_negative(self):
        rgx_anchor = Anchor(self.regex, negate=True)
        self.assertTrue(rgx_anchor == '\\b\\d{4}-\\w+.txt\\B')

    def test_anchor_with_comment(self):
        rgx_anchor = Anchor(self.regex).comment('Test comment')
        self.assertTrue(rgx_anchor == '^\\d{4}-\\w+.txt$(?#Test comment)')

        comment = Comment('Test comment')
        rgx_anchor = Anchor(self.regex).comment(comment)
        self.assertTrue(rgx_anchor == '^\\d{4}-\\w+.txt$(?#Test comment)')
