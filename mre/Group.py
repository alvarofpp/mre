from .Regex import Regex
from typing import Union


class Group(Regex):
    """Group class."""

    def __init__(self, regex: Union[str, Regex, int] = "", non_capturing: bool = False):
        nc = "?:" if non_capturing else ""

        if isinstance(regex, int):
            regex = self.back_references(regex)
        elif isinstance(regex, str):
            regex = nc + regex
        else:
            regex = nc + regex.get()

        super().__init__(regex)

    def __str__(self):
        """Magic method to print."""
        return self._format(self.rgx)

    def get(self):
        """Return regex."""
        return self._format(self.rgx)

    def quantifier(self, n: int = 0, m: int = 0, without_maximum: bool = False):
        """Quantify the regex."""
        rgx = self.rgx
        self.rgx = self._format(self.rgx)
        regex_return = super().quantifier(n, m, without_maximum)
        self.rgx = rgx

        return regex_return

    def _format(self, regex: str = ""):
        """Format regex."""
        return "({})".format(regex)
