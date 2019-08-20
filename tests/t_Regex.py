from mre import Regex

test = Regex("[A-z]")

# __eq__
assert test == "[A-z]"

# __iadd__
test += "{3}"
assert test == "[A-z]{3}"

# set
test._set_regex("[0-9]{5}")
assert test == "[0-9]{5}"

# __add__
test_cep = test + "-" + Regex("[0-9]{3}")
assert test_cep == "[0-9]{5}-[0-9]{3}"
