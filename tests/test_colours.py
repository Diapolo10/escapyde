"""Test colours."""

from __future__ import annotations

from escapyde.colours import BBLUE, BGREEN, BRED, FBLUE, FGREEN, FRED


def test_foreground_red(red_foreground_example_text: list[tuple[str, str]]):
    """Test that red foreground text is generated as expected."""
    for text, expected_result in red_foreground_example_text:
        result = str(FRED | text)
        assert result == expected_result, result


def test_foreground_green(green_foreground_example_text: list[tuple[str, str]]):
    """Test that green foreground text is generated as expected."""
    for text, expected_result in green_foreground_example_text:
        result = str(FGREEN | text)
        assert result == expected_result, result


def test_foreground_blue(blue_foreground_example_text: list[tuple[str, str]]):
    """Test that blue foreground text is generated as expected."""
    for text, expected_result in blue_foreground_example_text:
        result = str(FBLUE | text)
        assert result == expected_result, result


def test_background_red(red_background_example_text: list[tuple[str, str]]):
    """Test that red background text is generated as expected."""
    for text, expected_result in red_background_example_text:
        result = str(BRED | text)
        assert result == expected_result, result


def test_background_green(green_background_example_text: list[tuple[str, str]]):
    """Test that green foreground text is generated as expected."""
    for text, expected_result in green_background_example_text:
        result = str(BGREEN | text)
        assert result == expected_result, result


def test_background_blue(blue_background_example_text: list[tuple[str, str]]):
    """Test that blue foreground text is generated as expected."""
    for text, expected_result in blue_background_example_text:
        result = str(BBLUE | text)
        assert result == expected_result, result
