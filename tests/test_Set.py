import unittest
from mre import Regex, Quantifier, Set


class TestSet(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes.
        """
        self.digits = Regex("0-9")

    def test_Cep(self):
        """Verifica se o Set funciona.
        """
        cep = Set(self.digits).quantifier(5)\
              + Quantifier("-", 0, 1)\
              + Set(self.digits).quantifier(3)
        self.assertTrue(cep == "[0-9]{5}-?[0-9]{3}")

    def test_Cep_2(self):
        """Verifica se o Set funciona.
        """
        cep = Set(self.digits).quantifier(5)\
              + Set(self.digits).quantifier(3)
        self.assertTrue(cep == "[0-9]{5}[0-9]{3}")
