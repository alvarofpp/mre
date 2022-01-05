from abc import ABC
from typing import Tuple, Union


class RegexBase(ABC):
    """Base class."""

    # Metacharacter
    ANY = '.'
    DOT = '\\.'
    DIGIT = '\\d'
    WHITESPACE = '\\s'
    WORD_CHARS = '\\w'  # Equivalent [A-Za-z0-9_]
    SLASH = '\\/'

    # Metacharacter (Negate)
    NOT_DIGIT = '\\D'
    NOT_WHITESPACE = '\\S'
    NOT_WORD_CHARS = '\\W'

    # Quantifiers
    ZERO_OR_ONE = '?'
    ZERO_OR_MULTIPLE = '*'
    ONE_OR_MULTIPLE = '+'

    # Set
    HYPHEN = '\\-'

    def __init__(self, *regexs: Union[str, int, 'RegexBase']):
        self._init_attributes()
        self._handle_inputs(regexs)

    def _handle_inputs(self, inputs: Tuple) -> None:
        for regex in inputs:
            if isinstance(regex, RegexBase):
                self.rgx += regex.get()
            else:
                self.rgx += regex

    def __str__(self):
        """Magic method to print."""
        return self.get()

    def __eq__(self, other: Union[str, 'RegexBase']):
        """Operator == ."""
        if isinstance(other, RegexBase):
            return (self.get() == other.get())
        return (self.get() == other)

    def __iadd__(self, other: Union[str, 'RegexBase']):
        """Operator += ."""
        self.rgx += other.get() if isinstance(other, RegexBase) else str(other)
        return self

    def __add__(self, regex: Union[str, 'RegexBase']):
        """Operator + ."""
        if isinstance(regex, RegexBase):
            return RegexBase(self.get() + regex.get())
        return RegexBase(self.get() + regex)

    def _init_attributes(self):
        if not hasattr(self, 'rgx'):
            self.rgx = ''

    def get(self) -> str:
        """Return regex."""
        return self.rgx

    def quantifier_symbol(self, n: int = 0, m: int = 0, without_maximum: bool = False) -> str:
        """Quantify the regex."""
        if n == 0 and m == 1:
            return self.ZERO_OR_ONE
        elif n == 0 and without_maximum:
            return self.ZERO_OR_MULTIPLE
        elif n == 1 and without_maximum:
            return self.ONE_OR_MULTIPLE

        regex = str(n)
        if without_maximum:
            regex += ','
        elif not m <= n:
            regex += ',' + str(m)
        return '{' + regex + '}'

    def backreferences(self, group_n: int = 1) -> 'RegexBase':
        """Back reference to a group."""
        return RegexBase(self.rgx, '\\{}'.format(group_n))

    def _set_regex(self, regex: Union[str, 'RegexBase']):
        """Set regex value."""
        if isinstance(regex, RegexBase):
            self.rgx = regex.rgx
        else:
            self.rgx = str(regex)
