from unittest import TestCase
from mre import Regex, Quantifier, Set


class TestSet(TestCase):
    def setUp(self):
        self.digits = Regex("0-9")

    def test_Cep(self):
        cep = Set(self.digits).quantifier(5) \
              + Quantifier("-", 0, 1) \
              + Set(self.digits).quantifier(3)
        self.assertTrue(cep == "[0-9]{5}-?[0-9]{3}")

    def test_Cep_2(self):
        cep = Set(self.digits).quantifier(5) \
              + Set(self.digits).quantifier(3)
        self.assertTrue(cep == "[0-9]{5}[0-9]{3}")
