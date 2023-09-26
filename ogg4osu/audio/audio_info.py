import ffmpeg
from os import PathLike
from pathlib import Path


class AudioInfo:
    """Information about an audio file."""
    def __init__(self, file: PathLike) -> None:
        self.path = Path(file).resolve()

        probe_data = ffmpeg.probe(file)
        audio_stream = _find_audio_stream(probe_data["streams"])
        format = probe_data["format"]

        self.codec = audio_stream["codec_name"]
        self.duration = float(audio_stream["duration"])
        self.sample_rate = int(audio_stream["sample_rate"])
        self.bit_rate = int(format["bit_rate"])
        self.size = int(format["size"])
        

def _find_audio_stream(streams: list[dict]) -> dict:
    for stream in streams:
        if stream["codec_type"] == "audio":
            return stream
