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

    return parser.parse_args()
