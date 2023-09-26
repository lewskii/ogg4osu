import ffmpeg
from os import PathLike

# maximum enforced by the ranking criteria in bits per second
MAX_BITRATE = 208_000

# the base amount of delay added to all audio files
# the osu! editor doesn't like files with absolutely no delay
__BASE_DELAY = 200


def convert(infile: PathLike, outfile: PathLike):
    """Convert an audio file to OGG Vorbis."""

    input_audio = (
        ffmpeg
        .input(infile)
        .audio
        .filter('adelay', delays = __BASE_DELAY, all = 1) # delay all channels
    )
    
    output_audio = input_audio.output(
        outfile,
        acodec = 'libvorbis',
        aq = 6,
        ar = 48_000
    )

    output_audio.run(quiet=True, overwrite_output=True)


def __reasonable_sample_rate(original_sample_rate: int) -> int:
    """
    Choose a reasonable sample rate based on a given original one.

    Here, \"reasonable\" is meant in terms of file size, so any input of 48 kHz
    or less will be returned as is. A higher input will be reduced to either 48
    kHz or 41.1 kHz based on which one it is a multiple of, because integer
    ratios are apparently ideal for resampling.
    """

    if original_sample_rate <= 48_000:
        return original_sample_rate
    
    elif original_sample_rate % 41_100 == 0:
        return 41_100
    
    else:
        return 48_000

