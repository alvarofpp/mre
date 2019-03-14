from .Regex import Regex
from .Range import Range
from typing import Union


class Set(Regex):
    """Set class."""

    def __init__(self, regex: Union[str, Regex] = ""):
        if isinstance(regex, str):
            super().__init__(regex)
        else:
            super().__init__(regex.get())

        self.format = "[{}]"

    def __str__(self):
        """Magic method to print."""
        return self.format.format(self.rgx)

    def __add__(self, regex: Union[str, 'Regex']):
        """Operator + ."""
        rgx = Regex()
        if isinstance(regex, Regex):
            rgx._set_regex(self.format.format(self.rgx) + regex.rgx)
        else:
            rgx._set_regex(self.format.format(self.rgx) + regex)

        return rgx

    def quantifier(self, n: int = 0, m: int = 0, without_maximum: bool = False):
        """Quantify the regex."""
        rgx = self.rgx
        if n == 0 and m == 1:
            rgx += self.ZERO_OR_ONE
        elif n == 0 and without_maximum:
            rgx += self.ZERO_OR_MULTIPLE
        elif n == 1 and without_maximum:
            rgx += self.ONE_OR_MULTIPLE
        else:
            regex = str(n)
            if without_maximum:
                regex += ','
            elif not m <= n:
                regex += "," + str(m)
            rgx = "[" + rgx + "]{" + regex + "}"
        return Regex(rgx)
