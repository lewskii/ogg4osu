"""Tools for handling information about audio files.

Classes:

- AudioInfo: a container for information about audio files
"""
import ffmpeg
from os import PathLike
from pathlib import Path


class AudioInfo:
    """Information about an audio file, meant for use in conversion.

    A very selective wrapper for the JSON outputted by ffprobe.
    
    Instance variables:

    - codec: the codec the audio was encoded with
    - sample_rate: the sample rate of the audio in hertz
    - bit_rate: the bit rate of the file in bits per second
    - duration: the duration of the audio in seconds
    - size: the size of the file in bytes
    - path: the path to the file the the information concerns
    - json: the raw JSON outputted by ffprobe
    """

    def __init__(self, file: PathLike) -> None:
        self.path = Path(file).resolve()
        """The path to the file the the information concerns."""

        self.json: dict = ffmpeg.probe(file)
        """The raw JSON outputted by ffprobe."""

        audio_stream = _find_audio_stream(self.json["streams"])
        format = self.json["format"]

        self.codec: str = audio_stream["codec_name"]
        """The codec the audio was encoded with."""
        self.sample_rate = int(audio_stream["sample_rate"])
        """The sample rate of the audio in hertz."""
        self.bit_rate = int(format["bit_rate"])
        """The bit rate of the file in bits per second."""
        self.duration = float(audio_stream["duration"])
        """The duration of the audio in seconds."""
        self.size = int(format["size"])
        """The size of the file in bytes."""
        

def _find_audio_stream(streams: list[dict]) -> dict:
    """Find a dict that represents an audio stream from a list and return it.

    This function is only meant to work with the JSON output of ffprobe.
    """
    for stream in streams:
        if stream["codec_type"] == "audio":
            return stream
