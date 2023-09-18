"""Unit test fixtures"""

import pytest


@pytest.fixture()
def red_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    messages = (
        "Hello, world!",
        "I'm really feeling it!",
    )

    return [
        (
            message,
            f"\x1b[31;49m{message}\x1b[0m",
        )
        for message in messages
    ]


@pytest.fixture()
def green_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    messages = (
        "Tempus edax rerum.",
        "Time, the devourer of all things.",
    )

    return [
        (
            message,
            f"\x1b[32;49m{message}\x1b[0m",
        )
        for message in messages
    ]


@pytest.fixture()
def blue_foreground_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    messages = (
        "Oderint dum metuant.",
        "Let them hate so long as they fear.",
    )

    return [
        (
            message,
            f"\x1b[34;49m{message}\x1b[0m",
        )
        for message in messages
    ]


@pytest.fixture()
def red_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    messages = (
        "Sic semper tyrannis.",
        "Thus always to tyrants.",
    )

    return [
        (
            message,
            f"\x1b[39;41m{message}\x1b[0m",
        )
        for message in messages
    ]


@pytest.fixture()
def green_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    messages = (
        "Vincit qui se vincit.",
        "He conquers who conquers himself.",
    )

    return [
        (
            message,
            f"\x1b[39;42m{message}\x1b[0m",
        )
        for message in messages
    ]


@pytest.fixture()
def blue_background_example_text() -> list[tuple[str, str]]:
    """Returns a list of tuples containing a string and an expected result"""

    messages = (
        "Astra inclinant, sed non obligant.",
        "The stars incline us, they do not bind us.",
    )

    return [
        (
            message,
            f"\x1b[39;44m{message}\x1b[0m",
        )
        for message in messages
    ]
