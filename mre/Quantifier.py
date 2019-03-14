from .Regex import Regex


class Quantifier(Regex):
    """Classe de quantificadores."""

    def __init__(self, n: int = 0, m: int = 0, without_maximum: bool = False):
        regex = ""
        if n == 0 and m == 1:
            regex += self.ZERO_OR_ONE
        elif n == 0 and without_maximum:
            regex += self.ZERO_OR_MULTIPLE
        elif n == 1 and without_maximum:
            regex += self.ONE_OR_MULTIPLE
        else:
            regex = str(n)
            if without_maximum:
                regex += ','
            elif not m <= n:
                regex += "," + str(m)
            regex = "{" + regex + "}"

        super().__init__(regex)
