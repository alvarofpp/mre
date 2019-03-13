from mre import Regex, Quantifier

digits = Regex("[0-9]")

# n = 1
assert (digits + Quantifier()) == "[0-9]{1}"

# n = 1, m = 5
assert (digits + Quantifier(m=5)) == "[0-9]{1,5}"

# n = 2, at_minimum = True
assert (digits + Quantifier(2, at_minimum=True)) == "[0-9]{2,}"

test_cep = (digits + Quantifier(n=5)) + "-" + (digits + Quantifier(n=3))
assert test_cep == "[0-9]{5}-[0-9]{3}"