from . import audio
from argparse import ArgumentParser

def main():
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

    audio.convert(args.input, args.output)

if __name__ == "__main__":
    main()
