from .Regex import Regex
from typing import Union


class Anchor(Regex):
    """Anchor class."""

    def __init__(self, regex: Union[str, int, Regex] = "", negate: bool = False):
        if negate:
            self.first = "\\b"
            self.last = "\\B"
        else:
            self.first = "^"
            self.last = "$"
        super().__init__(regex)

    def get(self) -> str:
        """Return regex."""
        return "{}{}{}".format(self.first, self.rgx, self.last)
