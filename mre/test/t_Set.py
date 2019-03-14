from mre import Regex, Quantifier, Set

digits = Regex("0-9")

cep = Set(digits).quantifier(5) + Quantifier("-", 0, 1) + Set(digits).quantifier(3)
assert cep == "[0-9]{5}-?[0-9]{3}"

cep = Set(digits).quantifier(5) + Set(digits).quantifier(3)
assert cep == "[0-9]{5}[0-9]{3}"
