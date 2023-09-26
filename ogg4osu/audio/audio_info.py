import ffmpeg
from os import PathLike
from pathlib import Path


class AudioInfo:
    """
    Select information about an audio file, meant for use in conversion.
    
    Instance variables:

    codec: the codec the audio was encoded with

    sample_rate: the sample rate of the audio in hertz

    bit_rate: the bit rate of the file in bits per second

    duration: the duration of the audio in seconds

    size: the size of the file in bytes

    path: the path to the file the the information concerns

    json: the raw JSON output from ffprobe
    """

    def __init__(self, file: PathLike) -> None:
        self.path = Path(file).resolve()
        """The path to the file the the information concerns."""

        self.json = ffmpeg.probe(file)
        """The raw JSON output from ffprobe."""

        audio_stream = _find_audio_stream(self.json["streams"])
        format = self.json["format"]

        self.codec = audio_stream["codec_name"]
        self.sample_rate = int(audio_stream["sample_rate"])
        self.bit_rate = int(format["bit_rate"])
        self.duration = float(audio_stream["duration"])
        self.size = int(format["size"])
        

def _find_audio_stream(streams: list[dict]) -> dict:
    """
    Find a dict that represents an audio stream from a list and return it.
    """
    for stream in streams:
        if stream["codec_type"] == "audio":
            return stream
