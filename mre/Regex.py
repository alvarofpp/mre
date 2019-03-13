from abc import ABC


class Regex(ABC):
    """Classe base."""

    def __init__(self, regex=""):
        self.rgx = regex
        self._define_metacharacter()

    def __str__(self):
        """Magic method to print."""
        return self.rgx

    def __eq__(self, other):
        """Operator =."""
        return (self.rgx == other.rgx) if isinstance(other, Regex) else (self.rgx == other)

    def __iadd__(self, other):
        self.rgx += other.rgx if isinstance(other, Regex) else other
        return self

    def __add__(self, regex):
        """Operator +."""
        rgx = Regex()
        if isinstance(regex, Regex):
            rgx.set(self.rgx + regex.rgx)
        else:
            rgx.set(self.rgx + regex)

        return rgx

    def set(self, regex):
        self.rgx = regex

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

