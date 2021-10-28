from unittest import TestCase
from mre import Regex, Set, Group, Comment


class TestGroup(TestCase):
    def setUp(self):
        self.group_value = Group(
            Set(Regex.WORD_CHARS + Regex.WHITESPACE).quantifier(n=1, without_maximum=True)
        )

    def test_tag_header_one(self):
        groups = Group("<h1>") \
                 + self.group_value \
                 + Group("</h1>")
        self.assertTrue(groups == "(<h1>)([\\w\\s]+)(</h1>)")

    def test_non_capturing(self):
        groups_nc = Group("<h1>", non_capturing=True) \
                    + self.group_value \
                    + Group("</h1>", non_capturing=True)
        self.assertTrue(groups_nc == "(?:<h1>)([\\w\\s]+)(?:</h1>)")

    def test_reference(self):
        group_tag = Regex('<', Group('h[1-6]'), '>')
        group_ref = Group(group_tag, non_capturing=True) \
                    + self.group_value \
                    + Group(Regex('<', Regex.SLASH, 1, '>'), non_capturing=True)
        self.assertTrue(group_ref == "(?:<(h[1-6])>)([\\w\\s]+)(?:<\\/\\1>)")

    def test_backreference(self):
        group = Group('test') + 'test' + Group(1)
        self.assertTrue(group == "(test)test(\\1)")

    def test_named_group(self):
        named_group_tag = Regex('<', Group('h[1-6]').name("tag"), '>')
        regex = Group(named_group_tag, non_capturing=True) \
                + self.group_value \
                + Group("</h1>", non_capturing=True)
        self.assertTrue(regex == "(?:<(?P<tag>h[1-6])>)([\\w\\s]+)(?:</h1>)")

    def test_reference_named_group(self):
        named_group_tag = Regex('<', Group('h[1-6]').name("tag"), '>')
        reference_named_group = Regex('</', Group().backreference_named('tag'), '>')
        regex = Group(named_group_tag, non_capturing=True) \
                + self.group_value \
                + Group(reference_named_group, non_capturing=True)
        self.assertTrue(regex == "(?:<(?P<tag>h[1-6])>)([\\w\\s]+)(?:</(?P=tag)>)")

    def test_group_with_comment(self):
        group = Group('test').comment('Test comment')
        self.assertTrue(group == "(test)(?#Test comment)")

        comment = Comment('Test comment')
        group = Group('test').comment(comment)
        self.assertTrue(group == "(test)(?#Test comment)")

    def test_group_qunatifier(self):
        group = Group('test').quantifier(1, 2)
        self.assertTrue(group == "(test){1,2}")
