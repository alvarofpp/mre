from typing import Union

from .Comment import Comment
from .Regex import Regex


class Group(Regex):
    def __init__(self, regex: Union[str, int, Regex] = '', non_capturing: bool = False):
        self.group_name = ''
        nc = '?:' if non_capturing else ''

        if isinstance(regex, int):
            self._init_attributes()
            regex = Regex(nc, self.backreferences(regex))
        elif isinstance(regex, str):
            regex = nc + regex
        else:
            regex = nc + regex.get()

        super().__init__(regex)

    def get(self) -> str:
        named_rgx = self.group_name + self.rgx

        if self.rgx_comment is not None:
            return '({})'.format(named_rgx) + self.rgx_comment.get()

        return '({})'.format(named_rgx)

    def comment(self, comment: Union[str, Comment] = '') -> 'Group':
        new_regex = Group(self.rgx)
        new_regex.rgx_comment = comment if isinstance(comment, Comment) else Comment(comment)

        return new_regex

    def name(self, group_name: str) -> 'Group':
        self.group_name = '?P<{}>'.format(group_name)
        return self

    def backreference_named(self, group_name_reference: str) -> 'Group':
        self.group_name = '?P={}'.format(group_name_reference)
        return self
