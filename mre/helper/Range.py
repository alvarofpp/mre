from mre.Regex import Regex
from typing import Union


class Range(Regex):
    """Range class."""

    def __init__(self, min: Union[str, int] = 0, max: Union[str, int] = "z"):
        super().__init__(self._format(min, max))

    def numbers(self, min: int = 0, max: int = 9):
        return Range(min, max)

    def letters(self, min: chr = 'A', max: chr = 'z', uppercase: bool = False, lowercase: bool = False):
        if lowercase and uppercase:
            min = min.lower()
            max = max.upper()
        elif lowercase:
            min = min.lower()
            max = max.lower()
        elif uppercase:
            min = min.upper()
            max = max.upper()

        return Range(min, max)

    def _format(self, min: Union[str, int] = None, max: Union[str, int] = None):
        """Format regex."""
        return "{}-{}".format(min, max)
