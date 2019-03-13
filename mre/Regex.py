from abc import ABC
from typing import Union


class Regex(ABC):
    """Base class."""

    def __init__(self, regex: str = ""):
        self.rgx = regex
        self._define_metacharacter()

    def __str__(self):
        """Magic method to print."""
        return self.rgx

    def __eq__(self, other: Union[str, 'Regex']):
        """Operator = ."""
        return (self.rgx == other.rgx) if isinstance(other, Regex) else (self.rgx == other)

    def __iadd__(self, other: Union[str, 'Regex']):
        """Operator += ."""
        self.rgx += other.rgx if isinstance(other, Regex) else other
        return self

    def __add__(self, regex: Union[str, 'Regex']):
        """Operator + ."""
        rgx = Regex()
        if isinstance(regex, Regex):
            rgx.set(self.rgx + regex.rgx)
        else:
            rgx.set(self.rgx + regex)

        return rgx

    def set(self, regex: Union[str, 'Regex']):
        """Set regex value."""
        if isinstance(regex, Regex):
            self.rgx = regex.rgx
        else:
            self.rgx = str(regex)

    def _define_metacharacter(self):
        # Metacharacter
        self.ANY = "."
        self.DOT = "\."
        self.DIGIT = "\d"
        self.WHITESPACE = "\s"
        self.WORD_CHARS = "\w"  # Equivalent [A-Za-z0-9_]
        self.HYPHEN = "\-"

        # Metacharacter (Negate)
        self.NOT_DIGIT = "\D"
        self.NOT_WHITESPACE = "\S"
        self.NOT_WORD_CHARS = "\W"
