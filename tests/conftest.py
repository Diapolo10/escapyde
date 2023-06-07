"""Unit test fixtures"""

import pytest


@pytest.fixture()
def red_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[0;31mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[0;31mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def green_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[0;32mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[0;32mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def blue_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[0;34mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[0;34mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def red_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[0;41;0mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[0;41;0mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def green_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[0;42;0mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[0;42;0mI'm really feeling it!\x1b[0m",
        ),
    ]


@pytest.fixture()
def blue_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    return [
        (
            "Hello, world!",
            "\x1b[0;44;0mHello, world!\x1b[0m",
        ),
        (
            "I'm really feeling it!",
            "\x1b[0;44;0mI'm really feeling it!\x1b[0m",
        ),
    ]
