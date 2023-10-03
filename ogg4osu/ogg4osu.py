"""The main logic of the program."""
from . import audio
from .audio import AudioFile
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
        source_file = AudioFile(source)
        if source_file.is_rankable():
            print(f"{source_file} is already either rankable or doomed.")
        else:
            print(f"Converting {source_file} to {destination}...")
            audio.convert(source_file, destination)
            print(f"Done!")
    except ffmpegError as error:
        stderr = error.stderr.decode().strip()
        print(stderr)

if __name__ == "__main__":
    main()
