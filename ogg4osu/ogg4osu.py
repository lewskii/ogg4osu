"""The main logic of the program."""
from . import audio
from argparse import ArgumentParser
from ffmpeg import Error as ffmpegError

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

    try:
        audio.convert(args.source, args.destination)
    except ffmpegError as error:
        stderr = error.stderr.decode().strip()
        print("stderr:\n", stderr, sep='')

if __name__ == "__main__":
    main()
