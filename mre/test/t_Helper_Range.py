from mre import Regex, Set
from mre.helper import Range

digits_one = Regex("[0-9]")
digits_two = Set(Range().numbers())

# [0-9]
assert digits_one == digits_two

# CPF [0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}
all_digits = Set(Range(0, 9))
dot = Regex('.').quantifier(0, 1)
hyphen = Regex('-').quantifier(0, 1)

rgx_cpf = Regex(
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), hyphen,
    all_digits.quantifier(2),
)

assert rgx_cpf == "[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}"