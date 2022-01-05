from typing import Union

from .Comment import Comment
from .Regex import Regex


class Set(Regex):
    def __init__(self, regex: Union[str, int, Regex] = ''):
        super().__init__(regex)

    def get(self) -> str:
        if self.rgx_comment is not None:
            return '[{}]'.format(self.rgx) + self.rgx_comment.get()

        return '[{}]'.format(self.rgx)

    def comment(self, comment: Union[str, Comment] = '') -> 'Set':
        new_regex = Set(self.rgx)
        new_regex.rgx_comment = comment if isinstance(comment, Comment) else Comment(comment)

        return new_regex
