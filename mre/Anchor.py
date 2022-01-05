from typing import Union

from .Comment import Comment
from .Regex import Regex


class Anchor(Regex):
    def __init__(self, regex: Union[str, int, Regex] = '', negate: bool = False):
        if negate:
            self.first = '\\b'
            self.last = '\\B'
        else:
            self.first = '^'
            self.last = '$'
        super().__init__(regex)

    def get(self) -> str:
        if self.rgx_comment is not None:
            return '{}{}{}'.format(self.first, self.rgx, self.last) + self.rgx_comment.get()

        return '{}{}{}'.format(self.first, self.rgx, self.last)

    def comment(self, comment: Union[str, Comment] = '') -> 'Anchor':
        new_regex = Anchor(self.rgx)

        if isinstance(comment, str):
            new_regex.rgx_comment = Comment(comment)
        else:
            new_regex.rgx_comment = comment

        return new_regex
