from typing import Union

from mre.Regex import Regex


class Range(Regex):
    def __init__(self, minimum: Union[str, int] = 0, maximum: Union[str, int] = 9):
        super().__init__('{}-{}'.format(minimum, maximum))

    @staticmethod
    def digits(minimum: int = 0, maximum: int = 9):
        return Range(minimum, maximum)

    @staticmethod
    def letters(
        minimum: chr = 'A',
        maximum: chr = 'z',
        uppercase: bool = False,
        lowercase: bool = False,
    ):
        if lowercase and uppercase:
            minimum = minimum.upper()
            maximum = maximum.lower()
        elif lowercase:
            minimum = minimum.lower()
            maximum = maximum.lower()
        elif uppercase:
            minimum = minimum.upper()
            maximum = maximum.upper()

        return Range(minimum, maximum)
