from .Regex import Regex
from .Group import Group
from typing import Union


class Lookahead(Group):
    """Lookahead class."""

    def __init__(self, regex: Union[str, int, Regex] = "", must_not_include: bool = False):
        lookahead = "?!" if must_not_include else "?="

        if isinstance(regex, int):
            regex = self.backreferences(regex)
        elif isinstance(regex, str):
            regex = lookahead + regex
        else:
            regex = lookahead + regex.get()

        super().__init__(regex, non_capturing=False)
