import unittest
from mre import Regex


class TestRegex(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes.
        """
        self.regex = Regex("[A-z]")

    def test_eq(self):
        """Verifica se o método __eq__ funciona.
        """
        self.assertTrue(self.regex == "[A-z]")

    def test_iadd(self):
        """Verifica se o método __iadd__ funciona.
        """
        self.regex += "{3}"
        self.assertTrue(self.regex == "[A-z]{3}")

    def test_set(self):
        """Verifica se o método _set_regex funciona.
        """
        self.regex._set_regex("[0-9]{5}")
        self.assertTrue(self.regex == "[0-9]{5}")

    def test_add(self):
        """Verifica se o método __add__ funciona.
        """
        self.regex = Regex("[0-9]{5}") + "-" + Regex("[0-9]{3}")
        self.assertTrue(self.regex == "[0-9]{5}-[0-9]{3}")
