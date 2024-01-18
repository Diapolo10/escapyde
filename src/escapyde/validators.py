"""Validator functions."""

from __future__ import annotations

from collections.abc import Sequence

from escapyde import config


def valid_foreground_colour(value: int | Sequence[int]) -> bool:
    """Validate ANSI escape foreground values."""
    if isinstance(value, Sequence):
        return valid_rgb_value(value)

    if value > config.MAX_FOREGROUND_COLOUR_LITERAL + 60:
        return False

    return config.MIN_FOREGROUND_COLOUR_LITERAL <= value % 60 <= config.MAX_FOREGROUND_COLOUR_LITERAL


def valid_background_colour(value: int | Sequence[int]) -> bool:
    """Validate ANSI escape background values."""
    if isinstance(value, Sequence):
        return valid_rgb_value(value)

    if value > config.MAX_BACKGROUND_COLOUR_LITERAL + 60:
        return False

    return config.MIN_BACKGROUND_COLOUR_LITERAL <= value % 60 <= config.MAX_BACKGROUND_COLOUR_LITERAL


def valid_rgb_value(value: Sequence[int]) -> bool:
    """Validate RGB literals."""
    return (
        len(value) == config.VALID_RGB_SEQUENCE_LENGTH
        and max(value) <= config.MAX_RGB_VALUE
        and min(value) >= config.MIN_RGB_VALUE
    )
