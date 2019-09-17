import unittest
from mre import Regex, Quantifier


class TestQuantifier(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes.
        """
        self.digits = Regex("[0-9]")

    def test_Quantifier_One(self):
        """Verifica se o regex com Quantifier n=1 funciona.
        """
        self.assertTrue((self.digits + Quantifier(n=1)) == "[0-9]{1}")

    def test_Quantifier_One_Five(self):
        """Verifica se o regex com Quantifier n=1 e m=5 funciona.
        """
        self.assertTrue((self.digits + Quantifier(n=1, m=5)) == "[0-9]{1,5}")

    def test_Quantifier_Two_WithoutMaximum(self):
        """Verifica se o regex com Quantifier n=2 e without_maximum=True funciona.
        """
        self.assertTrue((self.digits + Quantifier(n=2, without_maximum=True)) == "[0-9]{2,}")

    def test_CEP(self):
        """Verifica se o regex de CEP funciona.
        """
        test_cep = (self.digits + Quantifier(n=5)) + "-" + (self.digits + Quantifier(n=3))
        self.assertTrue(test_cep == "[0-9]{5}-[0-9]{3}")

    def test_Quantifier_WithoutMaximum(self):
        """Verifica se o regex com Quantifier n=2 e without_maximum=True funciona.
        """
        self.assertTrue(self.digits.quantifier(without_maximum=True) == "[0-9]*")
