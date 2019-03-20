from .Regex import Regex
from typing import Union


class Anchor(Regex):
    """Anchor class."""

    def __init__(self, regex: Union[str, Regex] = "", negate: bool = False):
        if negate:
            self.first = "\\b"
            self.last = "\\B"
        else:
            self.first = "^"
            self.last = "$"
        super().__init__(regex)

    def __str__(self):
        """Magic method to print."""
        return self._format(self.rgx)

    def get(self):
        """Return regex."""
        return self._format(self.rgx)

    def _format(self, regex: str = ""):
        """Format regex."""
        return "{}{}{}".format(self.first, regex, self.last)
