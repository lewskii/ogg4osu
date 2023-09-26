import ffmpeg
from os import PathLike
from pathlib import Path


class AudioInfo:
    """Information about an audio file."""
    def __init__(self, file: PathLike) -> None:
        self.path = Path(file)

        probe_data = ffmpeg.probe(file)
        audio_stream = __find_audio_stream(probe_data["streams"])
        format = probe_data["format"]

        self.codec = audio_stream["codec_name"]
        self.duration = audio_stream["duration"]
        self.sample_rate = audio_stream["sample_rate"]
        self.bit_rate = format["bit_rate"]
        self.size = format["size"]
        

def __find_audio_stream(streams: list[dict]) -> dict:
    for stream in streams:
        if stream["codec_type"] == "audio":
            return stream
