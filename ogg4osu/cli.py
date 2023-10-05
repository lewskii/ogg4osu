"""Allows users to interact with the program through the command line.

Functions:

- parse_args: parse the arguments passed to the program
"""
from argparse import ArgumentParser, Namespace

def parse_args() -> Namespace:
    """Parse and return the arguments given when the program was run.

    Returns an argparse.Namespace with attributes corresponding to the
    following arguments:

    - source: the path to the file the user wants to convert
    - destination: the path the converted file will have (optional, None by
    default)
    - silence: whether the program should just detect the silence in the input
    file
    """
    parser = ArgumentParser(
        prog = "ogg4osu",
        description = "Converts audio to OGG Vorbis for the purposes of osu!"
    )
    parser.add_argument(
        "source",
        help = "the path to the file you want to convert"
    )
    parser.add_argument(
        "destination",
        nargs = '?',
        default = None,
        help = "the path the converted file will have (optional)"
    )
    parser.add_argument(
        "-s",
        "--silence",
        help = "detect silence for testing",
        action = "store_true"
    )

    return parser.parse_args()
