from .Regex import Regex
from typing import Union
from .Comment import Comment


class Set(Regex):
    """Set class."""

    def __init__(self, regex: Union[str, int, Regex] = ""):
        super().__init__(regex)

    def get(self) -> str:
        """Return regex."""
        if self.rgx_comment is not None:
            return "[{}]".format(self.rgx) + self.rgx_comment.get()

        return "[{}]".format(self.rgx)

    def quantifier(self, n: int = 0, m: int = 0, without_maximum: bool = False) -> Regex:
        """Quantify the regex."""
        rgx_old = self.rgx
        self.rgx = self.get()
        regex_return = super().quantifier(n, m, without_maximum)
        self.rgx = rgx_old

        return regex_return

    def comment(self, comment: Union[str, Comment] = "") -> 'Set':
        """Set comment for regex."""
        new_regex = Set(self.rgx)
        new_regex.rgx_comment = comment if isinstance(comment, Comment) else Comment(comment)

        return new_regex
