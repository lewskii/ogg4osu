# ogg4osu!

Do you prefer using OGG over MP3 in your osu! beatmaps? Do you want to just slap q6 on all of your audio files because it's the highest quality setting that's still rankable most of the time? Do you hate having to check whether your q6 OGGs are actually under the 208kbps limit? This program will do that for you.

## Installation

1. [Get FFmpeg](https://ffmpeg.org/download.html) and make sure it's accessible from your command line.
    
    On Windows, you'll need to [add FFmpeg to PATH](https://www.google.com/search?q=add+ffmpeg+to+path) for this to work. I have no idea how it's done on other platforms, but I hope it's easier than on Windows.

2. [Install Python](https://www.python.org/downloads/).

    Python 3.11 or later should work for sure; when in doubt, just get the latest version. Older versions may work as well, but you're on your own with those.

3. Install ogg4osu!

    The following command should be all you need:

        pip install ogg4osu

    If you want/need something more specialised, I'm sure you already know what you need to do differently.

## Usage

The following examples use the kind-of-maybe-somewhat universal `python` command, but depending on your environment and/or preferences, you may want to use `python3` or `py` instead.

### Just convert an audio file to OGG
    
    python -m ogg4osu example.flac

You'll get a new file called `example.ogg`.

### Specify the name of the new file

    python -m ogg4osu "long and inconvenient song title.flac" song.ogg

You can also go wild with full file paths if you want.

### View all available options

    python -m ogg4osu -h
