import unittest
from mre import Regex, Comment, Set


class TestComment(unittest.TestCase):

    def test_Comment_Method(self):
        """Tests the comment method.
        """
        # All digits
        digits = Regex("[0-9]")
        # CEP regex
        rgx_cep = Regex(
            digits.quantifier(5),
            Regex("-").quantifier(0, 1),
            digits.quantifier(3)
        ).comment('Get zip code Brazil on input')

        self.assertTrue(rgx_cep == "[0-9]{5}-?[0-9]{3}(?#Get zip code Brazil on input)")

    def test_Comment_Class(self):
        """Tests the Comment class.
        """
        # All digits
        digits = Regex("[0-9]")
        # CEP comment
        cep_comment = Comment('Get zip code Brazil on input')
        # CEP regex
        rgx_cep = Regex(
            digits.quantifier(5),
            Regex("-").quantifier(0, 1),
            digits.quantifier(3),
            cep_comment
        )

        self.assertTrue(rgx_cep == "[0-9]{5}-?[0-9]{3}(?#Get zip code Brazil on input)")

    def test_Set_comment(self):
        # All digits
        digits = Set(Regex("0-9"))
        # Add comment
        digits = digits.comment('Get all digits')

        self.assertTrue(digits == "[0-9](?#Get all digits)")
