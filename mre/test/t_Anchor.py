from mre import Regex, Quantifier, Anchor

regex = Regex(Quantifier(Regex.DIGIT, 4), '-', Quantifier(Regex.WORD_CHARS, 1, without_maximum=True), '.txt')

rgx_anchor = Anchor(regex)
assert rgx_anchor == "^\\d{4}-\\w+.txt$"

rgx_anchor_negate = Anchor(regex, negate=True)
assert rgx_anchor_negate == "\\b\\d{4}-\\w+.txt\\B"
