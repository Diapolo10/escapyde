"""A library for simplifying ANSI escape sequences in Python."""

import importlib

from escapyde.ansi import *
from escapyde.colours import *

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"
