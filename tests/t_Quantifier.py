from mre import Regex, Quantifier

digits = Regex("[0-9]")

# n = 1
assert (digits + Quantifier(n=1)) == "[0-9]{1}"

# n = 1, m = 5
assert (digits + Quantifier(n=1, m=5)) == "[0-9]{1,5}"

# n = 2, at_minimum = True
assert (digits + Quantifier(n=2, without_maximum=True)) == "[0-9]{2,}"

# CEP
test_cep = (digits + Quantifier(n=5)) + "-" + (digits + Quantifier(n=3))
assert test_cep == "[0-9]{5}-[0-9]{3}"

# quantifier method
assert Regex("[0-9]").quantifier(without_maximum=True) == "[0-9]*"
