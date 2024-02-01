"""Main ANSI Escape sequence class."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from escapyde.config import (
    ANSI_RESET_SEQUENCE,
    DEFAULT_BACKGROUND_COLOUR,
    DEFAULT_FOREGROUND_COLOUR,
    USE_RGB_BACKGROUND,
    USE_RGB_FOREGROUND,
)
from escapyde.validators import (
    valid_background_colour,
    valid_foreground_colour,
)

__all__ = ('AnsiEscape', 'escape_format')


class AnsiEscape:
    """Wrapper for ANSI escape sequences that makes use of operators as syntactic sugar."""

    def __init__(self: AnsiEscape,
                 foreground_colour: int | Sequence[int] = DEFAULT_FOREGROUND_COLOUR,
                 background_colour: int | Sequence[int] = DEFAULT_BACKGROUND_COLOUR,
                 string: str | None = None) -> None:
        """AnsiEscape instance."""
        if not valid_foreground_colour(foreground_colour):
            msg = 'Invalid foreground colour value'
            raise ValueError(msg)
        if not valid_background_colour(background_colour):
            msg = 'Invalid background colour value'
            raise ValueError(msg)

        self._foreground_colour = foreground_colour
        self._background_colour = background_colour
        self._string = string

    def __str__(self: AnsiEscape) -> str:
        """Sequence as string."""
        if self.string:
            return f"{self.sequence}{self.string}{ANSI_RESET_SEQUENCE}"

        return ""

    def __repr__(self: AnsiEscape) -> str:
        """Sequence string representation."""
        state = f'{self.foreground_colour=}, {self.background_colour=}, {self.string=}'
        return f'{self.__class__.__name__}({state})'

    def __or__(self: AnsiEscape, other: Any) -> AnsiEscape:
        """Chain operands."""
        if isinstance(other, AnsiEscape):
            foreground_colour = self.foreground_colour
            background_colour = self.background_colour

            if other.foreground_colour != DEFAULT_FOREGROUND_COLOUR:
                foreground_colour = other.foreground_colour

            if other.background_colour != DEFAULT_BACKGROUND_COLOUR:
                background_colour = other.background_colour

            string = self.string

            if self.string is not None and other.string is not None:
                string = str(self) + str(other)
            elif self.string is None:
                string = other.string

            return AnsiEscape(
                foreground_colour=foreground_colour,
                background_colour=background_colour,
                string=string,
            )

        return AnsiEscape(
            foreground_colour=self.foreground_colour,
            background_colour=self.background_colour,
            string=str(other),
        )

    def __ror__(self: AnsiEscape, other: Any) -> AnsiEscape:
        """Chain operands."""
        return self | other

    @property
    def sequence(self: AnsiEscape) -> str:
        """Handle the internal sequence."""
        foreground_colour: int | Sequence[int] | str = self.foreground_colour
        background_colour: int | Sequence[int] | str = self.background_colour

        if isinstance(foreground_colour, Sequence):
            # Foreground colour is in RGB values
            foreground_colour = f'{USE_RGB_FOREGROUND};2;' + ';'.join(str(num) for num in foreground_colour)

        if isinstance(background_colour, Sequence):
            # Background colour is in RGB values
            background_colour = f'{USE_RGB_BACKGROUND};2;' + ';'.join(str(num) for num in background_colour)

        return f"\033[{foreground_colour};{background_colour}m"

    @property
    def foreground_colour(self: AnsiEscape) -> int | Sequence[int]:
        """Foreground colour."""
        return self._foreground_colour

    @property
    def background_colour(self: AnsiEscape) -> int | Sequence[int]:
        """Background colour."""
        return self._background_colour

    @property
    def string(self: AnsiEscape) -> str | None:
        """Wrapped string."""
        return self._string


def escape_format(string: str, escape_map: dict[str, AnsiEscape], case_sensitive: bool = False) -> str:
    r"""
    Map a dictionary of substrings => escape sequences to the given string.

    Returns a new string with the sequences applied to all
    found substrings.

    Example:
    -------
    import escapyde as esc

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

    text = (
        "Hello, red world! The sun is bright yellow, and the sky cyan blue.\n"
        "Green, lush fields are all around us."
    )

    print(esc.escape_format(text, COLOURS))  # Would print all mapped words in their respective colours

    Inspired by: https://www.reddit.com/r/learnpython/comments/rvcg0l/print_colour_in_terminal/hr73v3f/

    """
    lines = string.splitlines()
    for line_idx, line in enumerate(lines):

        words = line.split(' ')
        for substring, escape in escape_map.items():

            for idx, word in enumerate(words):

                temp_word = word
                temp_substring = substring

                if not case_sensitive:
                    temp_substring = temp_substring.lower()
                    temp_word = temp_word.lower()

                if temp_word.startswith(temp_substring):
                    words[idx] = f'{escape | word[:len(substring)]}{word[len(substring):]}'

        lines[line_idx] = ' '.join(words)

    return '\n'.join(lines)
