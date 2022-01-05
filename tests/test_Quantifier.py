from unittest import TestCase

from mre import Quantifier, Regex


class TestQuantifier(TestCase):
    def setUp(self):
        self.digits = Regex('[0-9]')

    def test_quantifier_one(self):
        self.assertTrue((self.digits + Quantifier(n=1)) == '[0-9]{1}')

    def test_quantifier_one_five(self):
        self.assertTrue((self.digits + Quantifier(n=1, m=5)) == '[0-9]{1,5}')

    def test_quantifier_two_without_maximum(self):
        self.assertTrue((self.digits + Quantifier(n=2, without_maximum=True)) == '[0-9]{2,}')

    def test_CEP(self):
        test_cep = (self.digits + Quantifier(n=5)) + '-' + (self.digits + Quantifier(n=3))
        self.assertTrue(test_cep == '[0-9]{5}-[0-9]{3}')

    def test_quantifier_without_maximum(self):
        self.assertTrue(self.digits.quantifier(without_maximum=True) == '[0-9]*')
