import ffmpeg
from os import PathLike

# maximum enforced by the ranking criteria in bits per second
MAX_BITRATE = 208000

# the base amount of delay added to all audio files
# the osu! editor doesn't like files with absolutely no delay
__BASE_DELAY = 200

def convert(infile: PathLike, outfile: PathLike):
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
        ar = 48000
    )

    output_audio.run(quiet=True, overwrite_output=True)
