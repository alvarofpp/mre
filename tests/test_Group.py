import unittest
from mre import Regex, Set, Group


class TestGroup(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes.
        """
        self.group_value = Group(
            Set(Regex.WORD_CHARS + Regex.WHITESPACE).quantifier(n=1, without_maximum=True)
        )

    def test_Tag_H_One(self):
        """Verifica se o regex para a tag <h1> funciona.
        """
        groups = \
            Group("<h1>") \
            + self.group_value \
            + Group("</h1>")
        self.assertTrue(groups == "(<h1>)([\w\s]+)(</h1>)")

    def test_Non_Capturing(self):
        """Verifica se o regex para a tag <h1> com non-capturing funciona.
        """
        groups_nc = \
            Group("<h1>", non_capturing=True) \
            + self.group_value \
            + Group("</h1>", non_capturing=True)
        self.assertTrue(groups_nc == "(?:<h1>)([\w\s]+)(?:</h1>)")

    def test_Reference(self):
        """Verifica se o regex para a tag <h1> com non-capturing e referência funciona.
        """
        group_tag = Regex('<', Group('h[1-6]'), '>')
        group_ref = \
            Group(group_tag, non_capturing=True) \
            + self.group_value \
            + Group(Regex('<', Regex.SLASH, 1, '>'), non_capturing=True)

        self.assertTrue(group_ref == "(?:<(h[1-6])>)([\w\s]+)(?:<\/\\1>)")
