"""Tools for working with audio files.

Classes:

- AudioFile: represents an audio file

Functions:

- convert: convert an audio file to OGG Vorbis
"""
import ffmpeg
from os import PathLike
from pathlib import Path


# enforced by the ranking criteria
OGG_MAX_BIT_RATE = 208_000
MP3_MAX_BIT_RATE = 192_000


class AudioFile:
    """Provides easy access to select information about an audio file.

    Essentially a highly selective wrapper for the ffprobe output for the file.
    
    Instance variables:

    - path: the path to the file
    - codec: the codec the file was encoded with
    - sample_rate: the sample rate of the file in hertz
    - bit_rate: the bit rate of the file in bits per second
    - duration: the duration of the file in seconds
    - size: the size of the file in bytes
    - probe: the raw JSON outputted by ffprobe

    Methods:

    - converted_sample_rate: return the sample rate the file should be
    converted to
    - is_rankable: return whether the file is rankable
    """

    @classmethod
    def __find_audio_stream(cls, streams: list[dict]) -> dict:
        """Find a dict that represents an audio stream from a list and return it.

        This function is only meant to work with the JSON output of ffprobe.
        """
        for stream in streams:
            if stream["codec_type"] == "audio":
                return stream
            
    def __init__(self, file: PathLike) -> None:
        """Construct an AudioFile.

        Arguments:

        - file: the path to the file
        
        Exceptions:

        Raises an exception if the given path is invalid, ffprobe can't read the
        file, or the file doesn't contain an audio stream.
        """
        self.path = Path(file).resolve()

        self.probe: dict = ffmpeg.probe(file)

        audio_stream = AudioFile.__find_audio_stream(self.probe["streams"])
        format = self.probe["format"]

        self.codec: str = audio_stream["codec_name"]
        self.sample_rate = int(audio_stream["sample_rate"])
        self.bit_rate = int(format["bit_rate"])
        self.duration = float(audio_stream["duration"])
        self.size = int(format["size"])

    def __str__(self) -> str:
        return self.path.name

    def converted_sample_rate(self) -> int:
        """Return a reasonable sample rate to convert the file to.

        Here, \"reasonable\" is meant in terms of file size and certain
        considerations regarding resampling:
        - If the sample rate of the file is 48 kHz or less, it will be returned
        as is.
        - A higher sample rate will be reduced to either 48 kHz or 41.1 kHz
        based on which one it is a multiple of, because integer ratios are
        apparently ideal for resampling.
        """
        if self.sample_rate <= 48_000:
            return self.sample_rate
        
        elif self.sample_rate % 41_100 == 0:
            return 41_100
        
        else:
            return 48_000
        
    def is_rankable(self) -> bool:
        """Return whether the file is rankable based on its codec and bit rate.

        According to the Ranking Criteria, a map's audio must be one of the
        following:
        - An OGG Vorbis file with a bitrate of 208 kbps or lower, or
        - An MP3 file with a bitrate of 192 kbps or lower.

        If the file matches one of these descriptions, the method returns True.
        If the file uses a different codec or its bit rate is too high, the
        method returns False.

        Whether the file is good enough to be ranked is too complex of a matter
        to evaluate here.
        """
        match self.codec:
            case "vorbis":
                return self.bit_rate <= OGG_MAX_BIT_RATE
            case "mp3":
                return self.bit_rate <= MP3_MAX_BIT_RATE
            case _:
                return False


# the base amount of delay added to all converted files because
# the osu! editor doesn't like files with absolutely no delay
__BASE_DELAY = 200

def convert(source: PathLike | AudioFile, destination: PathLike) -> None:
    """Convert an audio file to OGG Vorbis.

    Arguments:

    - source: the path to or a representation of the file that will be converted
    - destination: the path the converted file will have

    Exceptions:

    Propagates any exceptions raised by ffmpeg or AudioInfo. This usually 
    happens because infile does not exist or the file it points to has no
    audio stream.
    """
    if type(source) != AudioFile:
        source = AudioFile(source)
    
    input_audio = (
        ffmpeg
        .input(str(source.path))
        .audio
        .filter('adelay', delays = __BASE_DELAY, all = 1) # delay all channels
    )

    output_audio = input_audio.output(
        str(destination),
        acodec = 'libvorbis',
        aq = 6,
        ar = source.converted_sample_rate()
    )

    output_audio.run(quiet=True, overwrite_output=True)

    output_file = AudioFile(destination)

    if not output_file.is_rankable():
        output_audio = input_audio.output(
            str(destination),
            acodec = 'libvorbis',
            aq = 5,
            ar = source.converted_sample_rate()
        )
        output_audio.run(quiet=True, overwrite_output=True)
