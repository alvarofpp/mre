from mre import Regex, Set, Group

digits = Regex("0-9")

# group + group
get_groups = \
    Group("<h1>")\
    + Group(
        Set(Regex.WORD_CHARS + Regex.WHITESPACE).quantifier(n=1, without_maximum=True)
    )\
    + Group("</h1>")

tag_h_one = "<h1>Hello World</h1>"
assert get_groups == "(<h1>)([\w\s]+)(</h1>)"
