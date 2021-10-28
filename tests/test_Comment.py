from unittest import TestCase
from mre import Regex, Comment, Set


class TestComment(TestCase):
    def test_comment_method(self):
        # All digits
        digits = Regex("[0-9]")
        # CEP regex
        rgx_cep = Regex(
            digits.quantifier(5),
            Regex("-").quantifier(0, 1),
            digits.quantifier(3)
        ).comment('Get zip code Brazil on input')

        self.assertTrue(rgx_cep == "[0-9]{5}-?[0-9]{3}(?#Get zip code Brazil on input)")

    def test_comment_class(self):
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

    def test_set_comment(self):
        # All digits
        digits = Set(Regex("0-9"))
        # Add comment
        digits = digits.comment('Get all digits')

        self.assertTrue(digits == "[0-9](?#Get all digits)")

    def test_comment_set_method(self):
        comment = Comment()
        comment.set('Test comment')
        self.assertTrue(comment.get() == "(?#Test comment)")
