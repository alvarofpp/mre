import unittest
from mre import Regex, Quantifier, Anchor


class TestAnchor(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes.
        """
        self.regex = Regex(Quantifier(Regex.DIGIT, 4), '-', Quantifier(Regex.WORD_CHARS, 1, without_maximum=True), '.txt')

    def test_Anchor(self):
        """Verifica se o Anchor funciona.
        """
        rgx_anchor = Anchor(self.regex)
        self.assertTrue(rgx_anchor == "^\\d{4}-\\w+.txt$")

    def test_Anchor_Negative(self):
        """Verifica se o Anchor com negative funciona.
        """
        rgx_anchor = Anchor(self.regex, negate=True)
        self.assertTrue(rgx_anchor == "\\b\\d{4}-\\w+.txt\\B")
