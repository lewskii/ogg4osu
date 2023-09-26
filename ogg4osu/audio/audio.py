"""Audio conversion tools.

Functions:

convert: convert an audio file to OGG Vorbis
"""
import ffmpeg
from os import PathLike
from .audio_info import AudioInfo

# the base amount of delay added to all audio files
# the osu! editor doesn't like files with absolutely no delay
__BASE_DELAY = 200


def convert(infile: PathLike, outfile: PathLike) -> None:
    """Convert an audio file to OGG Vorbis.

    Arguments:

    infile: the path to the file that will be converted

    outfile: the path where the result of the conversion will be

    Exceptions:

    Propagates any exceptions raised by ffmpeg or AudioInfo. This usually 
    happens because infile does not exist or the file it points to has no
    audio stream.
    """
    input_audio = (
        ffmpeg
        .input(str(infile))
        .audio
        .filter('adelay', delays = __BASE_DELAY, all = 1) # delay all channels
    )

    audio_info = AudioInfo(infile)
    
    output_audio = input_audio.output(
        str(outfile),
        acodec = 'libvorbis',
        aq = 6,
        ar = __reasonable_sample_rate(audio_info.sample_rate)
    )

    output_audio.run(quiet=True, overwrite_output=True)


def __reasonable_sample_rate(original_sample_rate: int) -> int:
    """Return a reasonable sample rate to convert to based on the original.

    Here, \"reasonable\" is meant in terms of file size; any input of 48 kHz
    or less will be returned as is. A higher input will be reduced to either 48
    kHz or 41.1 kHz based on which one it is a multiple of, because integer
    ratios are apparently ideal for resampling.

    Non-standard inputs are normalised to 48 kHz if they are over the limit and
    returned as-is otherwise.

    Arguments:

    original_sample_rate: the sample rate of the original audio file in hertz.
    """
    if original_sample_rate <= 48_000:
        return original_sample_rate
    
    elif original_sample_rate % 41_100 == 0:
        return 41_100
    
    else:
        return 48_000

