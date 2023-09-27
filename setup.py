import setuptools

with open("./README.md") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "ogg4osu",
    version = "0.1.0",
    description = "Converts audio to OGG Vorbis for the purposes of osu!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/lewskii/ogg4osu",
    author = "lewski",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities"
    ],
    keywords = "osu! convert music audio ogg",
    packages = setuptools.find_packages(),
    install_requires = ["ffmpeg-python"]
)
