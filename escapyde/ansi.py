"""Main ANSI Escape sequence class"""

from typing import Any, Dict, Iterable, Optional

__all__ = ('AnsiEscape', 'escape_format',)

_CLEAR: str = '\033[0m'


class AnsiEscape:
    """Wrapper for ANSI escape sequences that makes use of operators as syntactic sugar"""

    def __init__(self, colour: Optional[Iterable[int]] = None):
        self.sequence: str = f'\033[{";".join(str(rgb) for rgb in colour)}m' if colour is not None else ''
        self.string: Optional[str] = None

    def __str__(self) -> str:
        if self.string:
            return self.sequence + self.string + _CLEAR

        return ''

    def __or__(self, other: Any) -> 'AnsiEscape':
        if isinstance(other, AnsiEscape):
            self.sequence += other.sequence
            return self

        self.string = str(other)
        return self

    def __ror__(self, other: Any) -> 'AnsiEscape':
        return self.__or__(other)


def escape_format(string: str, escape_map: Dict[str, AnsiEscape], case_sensitive: bool=False) -> str:
    """
    Maps a dictionary of substrings => escape sequences to the given string,
    returning a new string with the sequences applied to all
    found substrings.

    Example:

    COLOURS = {
        'red': esc.FRED,
        'green': esc.FGREEN,
        'yellow': esc.FYELLOW,
        'blue': esc.FBLUE,
        'magenta': esc.FMAGENTA,
        'cyan': esc.FCYAN,
        'white': esc.FWHITE,
        'black': esc.FBLACK,
    }

    text = \"\"\"Hello, red world! The sun is bright yellow, and the sky cyan blue.
    Green, lush fields are all around us.\"\"\"

    print(escape_format(text, COLOURS))  # Would print all mapped words in their respective colours

    Inspired by: https://www.reddit.com/r/learnpython/comments/rvcg0l/print_colour_in_terminal/hr73v3f/
    """

    lines = string.splitlines()
    for line_idx, line in enumerate(lines):

        words = line.split(' ')
        for substring, escape in escape_map.items():

            for idx, word in enumerate(words):

                if not case_sensitive:
                    substring = substring.lower()
                    word = word.lower()

                if word.startswith(substring):
                    words[idx] = f'{escape | word[:len(substring)]}{word[len(substring):]}'

        lines[line_idx] = ' '.join(words)

    return '\n'.join(lines)
