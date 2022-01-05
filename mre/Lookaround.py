from typing import Union

from .Group import Group
from .Regex import Regex


class Lookahead(Group):
    def __init__(self, regex: Union[str, int, Regex] = '', must_not_include: bool = False):
        lookahead = '?!' if must_not_include else '?='

        if isinstance(regex, int):
            self._init_attributes()
            regex = Regex(lookahead, self.backreferences(regex))
        elif isinstance(regex, str):
            regex = lookahead + regex
        else:
            regex = lookahead + regex.get()

        super().__init__(regex, non_capturing=False)
