"""Test ANSI escapes"""

import pytest

from escapyde.ansi import AnsiEscape, escape_format
from escapyde.colours import BCYAN, FBLUE, FCYAN, FGREEN, FRED, FYELLOW


def test_escape_format_valid_case_insensitive():
    """Tests the happy path"""

    colours = {
        'red': FRED,
        'green': FGREEN,
        'yellow': FYELLOW,
        'blue': FBLUE,
        'cyan': FCYAN,
    }

    text = (
        "Hello, red world! "
        "The sun is bright yellow, and the sky cyan blue.\n"
        "Green, lush fields are all around us."
    )

    result = escape_format(text, colours)

    expected_result = (
        "Hello, \x1b[31;49mred\x1b[0m world! "
        "The sun is bright \x1b[33;49myellow\x1b[0m, and the sky \x1b[36;49mcyan\x1b[0m \x1b[34;49mblue\x1b[0m.\n"
        "\x1b[32;49mGreen\x1b[0m, lush fields are all around us."
    )

    assert result == expected_result, result


def test_escape_format_valid_case_sensitive():
    """Tests the happy path"""

    colours = {
        'red': FRED,
        'green': FGREEN,
        'yellow': FYELLOW,
        'blue': FBLUE,
        'cyan': FCYAN,
    }

    text = (
        "Hello, red world! "
        "The sun is bright yellow, and the sky cyan blue.\n"
        "Green, lush fields are all around us."
    )

    result = escape_format(text, colours, case_sensitive=True)

    expected_result = (
        "Hello, \x1b[31;49mred\x1b[0m world! "
        "The sun is bright \x1b[33;49myellow\x1b[0m, and the sky \x1b[36;49mcyan\x1b[0m \x1b[34;49mblue\x1b[0m.\n"
        "Green, lush fields are all around us."
    )

    assert result == expected_result, result


def test_mixed_foreground_background():
    """Tests mixing foreground and background colours"""

    foreground_colour = FRED
    background_colour = BCYAN
    mixed_colour = foreground_colour | background_colour

    assert foreground_colour.sequence == '\x1b[31;49m', foreground_colour.sequence
    assert background_colour.sequence == '\x1b[39;46m', background_colour.sequence
    assert mixed_colour.sequence == '\x1b[31;46m', mixed_colour.sequence

    text = "Hello, world!"

    result = str(mixed_colour | text)

    assert result == "\x1b[31;46mHello, world!\x1b[0m", result


def test_custom_colour():
    """Tests support for custom colours"""

    gold = AnsiEscape(foreground_colour=(0xDB, 0xAC, 0x34))
    white_gold = AnsiEscape(foreground_colour=37, background_colour=(0xDB, 0xAC, 0x34))

    result = str(gold | "This is gold!")

    assert result == "\x1b[38;2;219;172;52;49mThis is gold!\x1b[0m", result

    result = str(white_gold | "This is gold!")

    assert result == "\x1b[37;48;2;219;172;52mThis is gold!\x1b[0m", result
