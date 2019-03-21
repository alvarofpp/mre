from .Regex import Regex
from typing import Union


class Set(Regex):
    """Set class."""

    def __init__(self, regex: Union[str, int, Regex] = ""):
        super().__init__(regex)

    def get(self) -> str:
        """Return regex."""
        return "[{}]".format(self.rgx)

    def quantifier(self, n: int = 0, m: int = 0, without_maximum: bool = False) -> Regex:
        """Quantify the regex."""
        rgx_old = self.rgx
        self.rgx = self.get()
        regex_return = super().quantifier(n, m, without_maximum)
        self.rgx = rgx_old

        return regex_return
