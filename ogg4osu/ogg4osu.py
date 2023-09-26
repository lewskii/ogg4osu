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
        "input",
        help = "the name of the file you want to convert"
    )

    parser.add_argument(
        "output",
        help = "the name of the converted file"
    )

    args = parser.parse_args()

    try:
        audio.convert(args.input, args.output)
    except ffmpegError as error:
        stderr = error.stderr.decode().strip()
        print("stderr:\n", stderr, sep='')

if __name__ == "__main__":
    main()
