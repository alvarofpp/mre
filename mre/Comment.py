class Comment:
    """Comment class."""

    def __init__(self, raw_comment: str = ""):
        self.raw_comment = raw_comment

    def get(self) -> str:
        """Return regex."""
        return "(?#{})".format(self.raw_comment)

    def set(self, raw_comment: str = ""):
        """Set regex value."""
        self.raw_comment = raw_comment
