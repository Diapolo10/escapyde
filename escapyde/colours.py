from .ansi import AnsiEscape

sequence_table = {
    # Dark colours

    ## Foreground
    'fg_black': (0, 30),
    'fg_red': (0, 31),
    'fg_green': (0, 32),
    'fg_yellow': (0, 33),
    'fg_blue': (0, 34),
    'fg_magenta': (0, 35),
    'fg_cyan': (0, 36),
    'fg_white': (0, 37),

    ## Background
    'bg_black': (0, 40, 0),
    'bg_red': (0, 41, 0),
    'bg_green': (0, 42, 0),
    'bg_yellow': (0, 43, 0),
    'bg_blue': (0, 44, 0),
    'bg_magenta': (0, 45, 0),
    'bg_cyan': (0, 46, 0),
    'bg_white': (0, 47, 0),

    # Bright colours

    ## Foreground
    'fg_br_black': (0, 90),
    'fg_br_red': (0, 91),
    'fg_br_green': (0, 92),
    'fg_br_yellow': (0, 93),
    'fg_br_blue': (0, 94),
    'fg_br_magenta': (0, 95),
    'fg_br_cyan': (0, 96),
    'fg_br_white': (0, 97),

    ## Background
    'bg_br_black': (0, 100, 0),
    'bg_br_red': (0, 101, 0),
    'bg_br_green': (0, 102, 0),
    'bg_br_yellow': (0, 103, 0),
    'bg_br_blue': (0, 104, 0),
    'bg_br_magenta': (0, 105, 0),
    'bg_br_cyan': (0, 106, 0),
    'bg_br_white': (0, 107, 0),
}

RED = AnsiEscape(sequence_table['fg_red'])