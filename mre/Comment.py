from .RegexBase import RegexBase


class Comment(RegexBase):
    """Comment class."""

    def get(self) -> str:
        """Return regex."""
        return "(?#{})".format(self.rgx)
