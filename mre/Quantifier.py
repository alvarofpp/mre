from .Regex import Regex
from typing import Union


class Quantifier(Regex):
    """Quantifier class."""

    def __init__(self, regex: Union[str, int, Regex] = "", n: int = 0, m: int = 0, without_maximum: bool = False):
        super().__init__(regex)
        self._set_regex(self.quantifier(n, m, without_maximum))
