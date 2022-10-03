"""Contains the colors used in the program."""
from collections import defaultdict

RED = "red"
GREEN = "green"
YELLOW = "yellow"
BLUE = "blue"
MAGENTA = "magenta"
CYAN = "cyan"
GREY = "grey"
WHITE = "white"
BLACK = "black"

ERROR = RED
WARNING = YELLOW
SUCCESS = GREEN

DIFICULTY = {
    "easy": GREEN,
    "medium": YELLOW,
    "hard": RED,
    "insane": MAGENTA,
}

_OS = {
    "windows": BLUE,
    "linux": GREEN,
    "freebsd": MAGENTA,
    "openbsd": YELLOW,
    "other": CYAN,
}

OS = defaultdict(lambda: CYAN, _OS)

BOOL = {
    True: GREEN,
    False: RED,
}
