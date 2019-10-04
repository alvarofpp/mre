class Comment:
    """Comment Class."""

    def __init__(self, raw_comment: str = ""):
        self.raw_comment = raw_comment

    def set(self, raw_comment: str = "") -> 'Comment':
        self.raw_comment = raw_comment

    def get(self) -> str:
        return self.raw_comment
