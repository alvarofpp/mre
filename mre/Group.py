from .Regex import Regex
from typing import Union
from .Comment import Comment


class Group(Regex):
    """Group class."""

    def __init__(self, regex: Union[str, int, Regex] = "", non_capturing: bool = False):
        nc = "?:" if non_capturing else ""

        if isinstance(regex, int):
            regex = self.backreferences(regex)
        elif isinstance(regex, str):
            regex = nc + regex
        else:
            regex = nc + regex.get()

        super().__init__(regex)

    def get(self) -> str:
        """Return regex."""
        if self.rgx_comment is not None:
            return "({})".format(self.rgx) + self.rgx_comment.get()

        return "({})".format(self.rgx)

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
