"""Test ANSI escapes"""

import pytest

from escapyde.ansi import escape_format
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
        "Hello, \x1b[0;31mred\x1b[0m world! "
        "The sun is bright \x1b[0;33myellow\x1b[0m, and the sky \x1b[0;36mcyan\x1b[0m \x1b[0;34mblue\x1b[0m.\n"
        "\x1b[0;32mGreen\x1b[0m, lush fields are all around us."
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
        "Hello, \x1b[0;31mred\x1b[0m world! "
        "The sun is bright \x1b[0;33myellow\x1b[0m, and the sky \x1b[0;36mcyan\x1b[0m \x1b[0;34mblue\x1b[0m.\n"
        "Green, lush fields are all around us."
    )

    assert result == expected_result, result


@pytest.mark.skip()  # NOTE: Requires refactoring the class to be immutable
def test_mixed_foreground_background():
    """Tests mixing foreground and background colours"""

    foreground_colour = FRED
    background_colour = BCYAN
    mixed_colour = foreground_colour | background_colour

    assert foreground_colour.sequence == '\x1b[0;31m', foreground_colour.sequence
    assert background_colour.sequence == '\x1b[0;46;0m', background_colour.sequence
    assert mixed_colour.sequence == '\x1b[0;31m\x1b[0;46;0m', mixed_colour.sequence

    text = "Hello, world!"

    result = str(mixed_colour | text)

    assert result == "\x1b[0;31m\x1b[0;46;0mHello, world!\x1b[0m", result
