"""Main ANSI Escape sequence class"""

from typing import Optional, Iterable

__all__ = ('AnsiEscape',)

_CLEAR = '\033[0m'


class AnsiEscape:
    """Wrapper for ANSI escape sequences that makes use of operators as syntactic sugar"""

    def __init__(self, colour: Optional[Iterable[int]] = None):
        self.sequence: str = f'\033[{";".join(str(rgb) for rgb in colour)}m' if colour is not None else ''
        self.string: Optional[str] = None

    def __str__(self) -> str:
        if self.string:
            return self.sequence + self.string + _CLEAR

        return ''

    def __or__(self, other):
        if isinstance(other, str):
            self.string = other
            return self

        if isinstance(other, AnsiEscape):
            self.sequence += other.sequence
            return self

        raise TypeError(f"Not compatible with type '{other.__class__.__name__}'")

    def __ror__(self, other):
        return self.__or__(other)
