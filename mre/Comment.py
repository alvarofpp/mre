from .RegexBase import RegexBase


class Comment(RegexBase):
    def get(self) -> str:
        return '(?#{})'.format(self.rgx)
