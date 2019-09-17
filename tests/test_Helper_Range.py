import unittest
from mre import Regex, Set
from mre.helper import Range


class TestHelperRange(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes.
        """
        self.regex = Regex("[0-9]")

    def test_Range_Digits(self):
        """Verifica se o Helper de Ranges funciona.
        """
        self.assertTrue(self.regex == Set(Range().digits()))

    def test_CPF(self):
        """Verifica se os modos de criar uma máscara para CPF funcionam.
        CPF [0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}
        """
        self.assertTrue(self.regex == Set(Range().digits()))
        all_digits = Set(Range(0, 9))
        dot = Regex('.').quantifier(0, 1)
        hyphen = Regex('-').quantifier(0, 1)

        rgx_cpf = Regex(
            all_digits.quantifier(3), dot,
            all_digits.quantifier(3), dot,
            all_digits.quantifier(3), hyphen,
            all_digits.quantifier(2),
        )
        self.assertTrue(rgx_cpf == "[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}")
