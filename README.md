# escapyde

Yet another ANSI escape sequence library for Python - now modernised!

## Installation

The package is readily available on PyPI. There are no dependencies, but Python 3.9 or newer is required.

On Windows:

```sh
py -m pip install escapyde
```

On other platforms:

```sh
pip3 install escapyde
```

## Changelog

You can find the project changelog [here][changelog].

## Usage

For basic usage, pre-made colours are available for your convenience.
Use them with the pipe operator on strings you want to colour. They
end the colour changes automatically, too!

```py
import escapyde
from escapyde.examples.text import SKULL

some_text = "Hello, world!"

print(f"I want to print this red: {escapyde.FRED | some_text}, and this yellow: {escapyde.FYELLOW | 'Hi!'}.")

print(f"Here's a cyan skull:\n{escapyde.FCYAN | SKULL}")
```

You can also colour backgrounds,

```py
import escapyde

some_more_text = "This should have a blue background."

print(f"{escapyde.BBLUE | some_more_text}")
```

combine formatting options,

```py
import escapyde

even_more_text = "Lorem Ipsum dolor sit amet."

print(f"{escapyde.FRED | escapyde.BWHITE | even_more_text}")
```

and even mix formatting options on the fly (although at present you need to
separate strings with parentheses):

```py
import escapyde

print(f"{(escapyde.FRED | 'Hello') | (escapyde.FBLUE | 'World')}")
```

It is possible to use custom foreground and background colours via the
`escapyde.AnsiEscape` class; these can be either valid ANSI literals or
RGB values:

```py
from escapyde.ansi import AnsiEscape
from escapyde.colours import sequence_table

fg_white = sequence_table['fg_white']  # You can alternatively use raw integers, eg. 37 for white

gold = AnsiEscape(foreground_colour=(0xDB, 0xAC, 0x34))
white_gold = AnsiEscape(foreground_colour=fg_white, background_colour=(219, 172, 34))

print(gold | "This is gold!")
print(white_gold | "This is white text on gold background!")
```

The class defaults to the default colours of the terminal,
so you don't need to set both values.

Finally, if you have a string with multiple substrings you wish to recolour, there's a function for that:

```py
from escapyde.ansi import AnsiEscape, escape_format

mapping = {
    'match': AnsiEscape(foreground_colour=(255, 0, 0)),
    'case': AnsiEscape(foreground_colour=(255, 255, 0)),
    'print': AnsiEscape(foreground_colour=(0, 255, 0)),
}

text = """
stuff = [3, 1, 4]

match stuff:
    case [3, *rest]:
        print("It's pi-like")
    case _:
        print("Not like pi")
"""

print(escape_format(string=text, escape_map=mapping, case_sensitive=True))
```

## Screenshots

![A screenshot of the example run on IPython on Windows.][old_screenshot]
![A screenshot of the newer examples run on IPython on Windows.][new_screenshot]
![A screenshot of the newer examples run on IPython on Windows.][new_screenshot_2]

[changelog]: ./CHANGELOG.md
[old_screenshot]: ./docs/assets/readme_screenshot.png "Not bad, not bad at all."
[new_screenshot]: ./docs/assets/readme_20230608.png "That's colour over there!"
[new_screenshot_2]: ./docs/assets/readme_20230608_2.png "That's colour over there!"
