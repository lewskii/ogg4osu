"""The main logic of the program."""
from . import audio
from . import cli
from ffmpeg import Error as ffmpegError
from pathlib import Path

def main():
    """Run ogg4osu with arguments from the command line."""
    args = cli.parse_args()

    source = Path(args.source)
    if not args.destination:
        destination = source.with_suffix(".ogg")
    else:
        destination = Path(args.destination)

    try:
        audio.convert(source, destination)
    except ffmpegError as error:
        stderr = error.stderr.decode().strip()
        print(stderr)

if __name__ == "__main__":
    main()
