"""Tools for working with audio files.

Modules:

- audio: audio conversion tools
- audio_info: for handling information about audio files

Classes:

- AudioInfo: a container for information about audio files

Functions:

- convert: convert an audio file to OGG Vorbis
"""
from .audio import convert
from .audio_info import AudioInfo
