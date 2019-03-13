from .Regex import Regex


class Quantifier(Regex):
    """Classe de quantificadores."""

    def __init__(self, n: int = 1, m: int = 0, at_minimum: bool = False):
        regex = str(n)

        if at_minimum:
            regex += ','
        elif not m <= n:
            regex += "," + str(m)

        regex = "{" + regex + "}"
        super().__init__(regex)
