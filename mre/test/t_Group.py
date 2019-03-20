from mre import Regex, Set, Group

# # group + group
group_value = Group(
    Set(Regex.WORD_CHARS + Regex.WHITESPACE).quantifier(n=1, without_maximum=True)
)
groups = \
    Group("<h1>") \
    + group_value \
    + Group("</h1>")

# tag_h_one = "<h1>Hello World</h1>"
assert groups == "(<h1>)([\w\s]+)(</h1>)"

# group + group with non-capturing
groups_nc = \
    Group("<h1>", non_capturing=True) \
    + group_value \
    + Group("</h1>", non_capturing=True)

assert groups_nc == "(?:<h1>)([\w\s]+)(?:</h1>)"

group_tag = Regex('<', Group('h[1-6]'), '>')

group_ref = \
    Group(group_tag, non_capturing=True) \
    + group_value \
    + Group(Regex('<', Regex.SLASH, 1, '>'), non_capturing=True)

assert group_ref == "(?:<(h[1-6])>)([\w\s]+)(?:<\/\\1>)"
