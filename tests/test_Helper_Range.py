from unittest import TestCase

from mre import Regex, Set
from mre.helpers import Range


class TestHelperRange(TestCase):
    def test_digits(self):
        regex = Regex('[0-9]')
        self.assertTrue(regex == Set(Range().digits()))

    def test_letters(self):
        self.assertTrue(Regex('[A-z]') == Set(Range().letters(uppercase=True, lowercase=True)))
        self.assertTrue(Regex('[A-Z]') == Set(Range().letters(uppercase=True, lowercase=False)))
        self.assertTrue(Regex('[a-z]') == Set(Range().letters(uppercase=False, lowercase=True)))
        self.assertTrue(Regex('[A-z]') == Set(Range().letters(uppercase=False, lowercase=False)))

    def test_CPF(self):
        all_digits = Set(Range(0, 9))
        dot = Regex('.').quantifier(0, 1)
        hyphen = Regex('-').quantifier(0, 1)

        rgx_cpf = Regex(
            all_digits.quantifier(3), dot,
            all_digits.quantifier(3), dot,
            all_digits.quantifier(3), hyphen,
            all_digits.quantifier(2),
        )
        self.assertTrue(rgx_cpf == '[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}')
