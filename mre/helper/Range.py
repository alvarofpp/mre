from mre.Regex import Regex
from typing import Union


class Range(Regex):
    """Range class."""

    def __init__(self, minimum: Union[str, int] = 0, maximum: Union[str, int] = "z"):
        super().__init__(self._format(minimum, maximum))

    def numbers(self, minimum: int = 0, maximum: int = 9):
        return Range(minimum, maximum)

    def letters(self, minimum: chr = 'A', maximum: chr = 'z', uppercase: bool = False, lowercase: bool = False):
        if lowercase and uppercase:
            minimum = minimum.lower()
            maximum = maximum.upper()
        elif lowercase:
            minimum = minimum.lower()
            maximum = maximum.lower()
        elif uppercase:
            minimum = minimum.upper()
            maximum = maximum.upper()

        return Range(minimum, maximum)

    def _format(self, minimum: Union[str, int] = None, maximum: Union[str, int] = None):
        """Format regex."""
        return "{}-{}".format(minimum, maximum)
