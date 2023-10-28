"""Sequences for colours and text formatting."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

from escapyde.ansi import AnsiEscape

__all__ = (
    'FBLACK', 'FRED', 'FGREEN', 'FYELLOW',
    'FBLUE', 'FMAGENTA', 'FCYAN', 'FWHITE',
    'BBLACK', 'BRED', 'BGREEN', 'BYELLOW',
    'BBLUE', 'BMAGENTA', 'BCYAN', 'BWHITE',
    'CLEAR',
)

sequence_table: dict[str, int | Sequence[int]] = {
    # Dark colours

    # Foreground
    'fg_black': 30,
    'fg_red': 31,
    'fg_green': 32,
    'fg_yellow': 33,
    'fg_blue': 34,
    'fg_magenta': 35,
    'fg_cyan': 36,
    'fg_white': 37,

    # Background
    'bg_black': 40,
    'bg_red': 41,
    'bg_green': 42,
    'bg_yellow': 43,
    'bg_blue': 44,
    'bg_magenta': 45,
    'bg_cyan': 46,
    'bg_white': 47,

    # Bright colours

    # Foreground
    'fg_br_black': 90,
    'fg_br_red': 91,
    'fg_br_green': 92,
    'fg_br_yellow': 93,
    'fg_br_blue': 94,
    'fg_br_magenta': 95,
    'fg_br_cyan': 96,
    'fg_br_white': 97,

    # Background
    'bg_br_black': 100,
    'bg_br_red': 101,
    'bg_br_green': 102,
    'bg_br_yellow': 103,
    'bg_br_blue': 104,
    'bg_br_magenta': 105,
    'bg_br_cyan': 106,
    'bg_br_white': 107,
}

FBLACK: AnsiEscape = AnsiEscape(foreground_colour=sequence_table['fg_black'])
FRED: AnsiEscape = AnsiEscape(foreground_colour=sequence_table['fg_red'])
FGREEN: AnsiEscape = AnsiEscape(foreground_colour=sequence_table['fg_green'])
FYELLOW: AnsiEscape = AnsiEscape(foreground_colour=sequence_table['fg_yellow'])
FBLUE: AnsiEscape = AnsiEscape(foreground_colour=sequence_table['fg_blue'])
FMAGENTA: AnsiEscape = AnsiEscape(foreground_colour=sequence_table['fg_magenta'])
FCYAN: AnsiEscape = AnsiEscape(foreground_colour=sequence_table['fg_cyan'])
FWHITE: AnsiEscape = AnsiEscape(foreground_colour=sequence_table['fg_white'])

BBLACK: AnsiEscape = AnsiEscape(background_colour=sequence_table['bg_black'])
BRED: AnsiEscape = AnsiEscape(background_colour=sequence_table['bg_red'])
BGREEN: AnsiEscape = AnsiEscape(background_colour=sequence_table['bg_green'])
BYELLOW: AnsiEscape = AnsiEscape(background_colour=sequence_table['bg_yellow'])
BBLUE: AnsiEscape = AnsiEscape(background_colour=sequence_table['bg_blue'])
BMAGENTA: AnsiEscape = AnsiEscape(background_colour=sequence_table['bg_magenta'])
BCYAN: AnsiEscape = AnsiEscape(background_colour=sequence_table['bg_cyan'])
BWHITE: AnsiEscape = AnsiEscape(background_colour=sequence_table['bg_white'])

CLEAR: AnsiEscape = AnsiEscape()
