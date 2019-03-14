from .Regex import Regex
from typing import Union


class Group(Regex):
    """Group class."""

    def __init__(self, regex: Union[str, Regex] = ""):
        if isinstance(regex, str):
            super().__init__(regex)
        else:
            super().__init__(regex.get())

    def __str__(self):
        """Magic method to print."""
        return self._format(self.rgx)

    def get(self):
        """Return regex."""
        return self._format(self.rgx)

    def quantifier(self, n: int = 0, m: int = 0, without_maximum: bool = False):
        """Quantify the regex."""
        rgx = self._format(self.rgx)
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
            rgx += "{" + regex + "}"
        return Regex(rgx)

    def _format(self, regex: str = ""):
        """Format regex."""
        return "({})".format(regex)
