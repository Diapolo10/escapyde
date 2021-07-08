"""Main ANSI Escape sequence class"""

CLEAR = f'\033[0m'

class AnsiEscape:
    def __init__(self, colour=None):
        self.sequence = f'\033[{";".join(str(rgb) for rgb in colour)}m'
        self.string = None

    def __str__(self):
        if self.string:
            return self.sequence + self.string + CLEAR

        return ''

    def __or__(self, other):
        if isinstance(other, str):
            self.string = other
            return self
        else:
            raise TypeError(f"Not compatible with type '{other.__class__.__name__}'")

    def __ror__(self, other):
        return self.__or__(other) 