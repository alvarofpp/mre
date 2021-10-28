from .Regex import Regex
from typing import Union
from .Comment import Comment


class Group(Regex):
    """Group class."""

    def __init__(self, regex: Union[str, int, Regex] = "", non_capturing: bool = False):
        self.group_name = ""
        nc = "?:" if non_capturing else ""

        if isinstance(regex, int):
            self._init_attributes()
            regex = Regex(nc, self.backreferences(regex))
        elif isinstance(regex, str):
            regex = nc + regex
        else:
            regex = nc + regex.get()

        super().__init__(regex)

    def get(self) -> str:
        """Return regex."""
        named_rgx = self.group_name + self.rgx

        if self.rgx_comment is not None:
            return "({})".format(named_rgx) + self.rgx_comment.get()

        return "({})".format(named_rgx)

    def quantifier(self, n: int = 0, m: int = 0, without_maximum: bool = False) -> Regex:
        """Quantify the regex."""
        rgx_old = self.rgx
        self.rgx = self.get()
        regex_return = super().quantifier(n, m, without_maximum)
        self.rgx = rgx_old

        return regex_return

    def comment(self, comment: Union[str, Comment] = "") -> 'Group':
        """Set comment for regex."""
        new_regex = Group(self.rgx)

        if isinstance(comment, str):
            new_regex.rgx_comment = Comment(comment)
        else:
            new_regex.rgx_comment = comment

        return new_regex

    def name(self, group_name: str) -> 'Group':
        """Set a group name."""
        self.group_name = "?P<{}>".format(group_name)
        return self

    def backreference_named(self, group_name_reference: str) -> 'Group':
        """Backreference by group name."""
        self.group_name = "?P={}".format(group_name_reference)
        return self
