from . import audio
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
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
