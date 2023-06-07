"""Unit test fixtures"""

import pytest


@pytest.fixture()
def red_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[31;49mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[31;49mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def green_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[32;49mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[32;49mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def blue_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[34;49mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[34;49mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def red_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[39;41mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[39;41mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def green_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[39;42mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[39;42mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def blue_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[39;44mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[39;44mI'm really feeling it!\x1b[0m",
        ),
    ]
