import unittest
from mre import Regex, Lookahead


class TestGroup(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes.
        """
        self.regex = Regex("[A-z]")


    def test_Positive_Lookahead(self):
        """Verifica se o regex para positive lookhead funciona.
        """
        lookahead = self.regex + Lookahead("water", must_not_include=False)
        self.assertTrue(lookahead == "[A-z](?=water)")

    def test_Negative_Lookahead(self):
        """Verifica se o regex para negative lookahead funciona.
        """
        lookahead = self.regex + Lookahead("water", must_not_include=True)
        self.assertTrue(lookahead == "[A-z](?!water)")
