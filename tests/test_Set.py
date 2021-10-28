from unittest import TestCase
from mre import Regex, Quantifier, Set, Comment


class TestSet(TestCase):
    def setUp(self):
        self.digits = Regex("0-9")

    def test_CEP(self):
        cep = Set(self.digits).quantifier(5) \
              + Quantifier("-", 0, 1) \
              + Set(self.digits).quantifier(3)
        self.assertTrue(cep == "[0-9]{5}-?[0-9]{3}")

        cep = Set(self.digits).quantifier(5) \
              + Set(self.digits).quantifier(3)
        self.assertTrue(cep == "[0-9]{5}[0-9]{3}")

    def test_set_with_comment(self):
        cep = Set(self.digits).quantifier(5) \
              + Quantifier("-", 0, 1) \
              + Set(self.digits).quantifier(3)

        cep_with_comment = cep.comment('Brazilian postal code')
        self.assertTrue(cep_with_comment == "[0-9]{5}-?[0-9]{3}(?#Brazilian postal code)")

    def test_set_with_comment_class(self):
        cep = Set(self.digits).quantifier(5) \
              + Quantifier("-", 0, 1) \
              + Set(self.digits).quantifier(3)

        comment = Comment('Brazilian postal code')
        cep_with_comment = cep.comment(comment)
        self.assertTrue(cep_with_comment == "[0-9]{5}-?[0-9]{3}(?#Brazilian postal code)")
