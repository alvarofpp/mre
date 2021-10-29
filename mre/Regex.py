from typing import Union, Tuple
from .RegexBase import RegexBase
from .Comment import Comment


class Regex(RegexBase):
    def __add__(self, regex: Union[str, 'Regex']):
        """Operator + ."""
        if isinstance(regex, Regex):
            return Regex(self.get() + regex.get())
        return Regex(self.get() + regex)

    def _handle_inputs(self, inputs: Tuple) -> None:
        for regex in inputs:
            if isinstance(regex, RegexBase):
                self.rgx += regex.get()
            elif isinstance(regex, int):
                self.rgx = self.backreferences(regex).get()
            else:
                self.rgx += regex

    def _init_attributes(self):
        super()._init_attributes()
        if not hasattr(self, 'rgx_comment'):
            self.rgx_comment = None

    def get(self) -> str:
        """Return regex."""
        if self.rgx_comment is None:
            return self.rgx

        return self.rgx + self.rgx_comment.get()

    def comment(self, comment: Union[str, Comment] = "") -> 'Regex':
        """Set comment for regex."""
        new_regex = Regex(self.rgx)
        new_regex.rgx_comment = comment if isinstance(comment, Comment) else Comment(comment)

        return new_regex

    def quantifier(self, n: int = 0, m: int = 0, without_maximum: bool = False) -> 'Regex':
        """Quantify the regex."""
        rgx = self.get() + self.quantifier_symbol(n, m, without_maximum)

        return Regex(rgx)
