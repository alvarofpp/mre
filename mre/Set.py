from .Regex import Regex
from typing import Union


class Set(Regex):
    """Set class."""

    def __init__(self, regex: Union[str, Regex] = ""):
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
        return "[{}]".format(regex)
