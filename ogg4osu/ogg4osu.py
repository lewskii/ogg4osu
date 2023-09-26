"""The main logic of the program."""
from . import audio
from argparse import ArgumentParser
from ffmpeg import Error as ffmpegError
from pathlib import Path

def main():
    """Run ogg4osu with arguments from the command line."""
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
    args = parser.parse_args()

    source = Path(args.source)
    if not args.destination:
        destination = source.with_suffix(".ogg")
    else:
        destination = Path(args.destination)

    try:
        audio.convert(source, destination)
    except ffmpegError as error:
        stderr = error.stderr.decode().strip()
        print("stderr:\n", stderr, sep='')

if __name__ == "__main__":
    main()
