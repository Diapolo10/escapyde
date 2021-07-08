"""Main ANSI Escape sequence class"""

from typing import Optional, List

CLEAR = f'\033[0m'

class AnsiEscape:
    def __init__(self, colour: Optional[List[int]] = None):
        self.sequence: str = f'\033[{";".join(str(rgb) for rgb in colour)}m' if colour is not None else ''
        self.string: Optional[str] = None

    def __str__(self) -> str:
        if self.string:
            return self.sequence + self.string + CLEAR

        return ''

    def __or__(self, other):
        if isinstance(other, str):
            self.string = other
            return self
        else:
            raise TypeError(f"Not compatible with type '{other.__class__.__name__}'")

    def __ror__(self, other):
        return self.__or__(other)
