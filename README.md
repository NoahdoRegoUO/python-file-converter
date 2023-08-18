<img align="right" src="logo.png" width="60px" height="81px">

# Python File Converter

## Description

An interactive command line program that is used to convert file types. The program will loop through any files that have been added
to the "input" folder, ask you to select your desired conversions (example: MOV -> GIF), and create the resulting files in the
"output" folder.

The program is built with the ffmpeg-python library, which provides Python bindings for FFmpeg commands.

## Usage

Prerequisites: to run this program, you'll need [Git](https://git-scm.com) and [Python 3](https://www.python.org/downloads/) installed.

From your command line / terminal:

1. Clone the directory with Git
2. [optional] remove the .gitkeep files from input and output directories
3. Add your desired file(s) to convert to the "input" folder
4. Install the ffmpeg-python library with `pip install ffmpeg-python`
5. Run the program with `python3 convert.py` and choose your desired conversions

## Version

Version `0.1.0` - Supported conversions:

- MP4 --> MP3 / GIF
- MOV --> MP3 / GIF

## License

MIT

---

> [noahdorego.com](https://www.noahdorego.com)
