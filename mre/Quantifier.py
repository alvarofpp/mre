from .Regex import Regex


class Quantifier(Regex):
    """Quantifier class."""

    def __init__(self, regex: str = "", n: int = 0, m: int = 0, without_maximum: bool = False):
        super().__init__(regex)
        self._set_regex(self.quantifier(n, m, without_maximum))
