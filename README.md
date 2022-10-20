# MediaInfo-Paste
Generates the mediainfo of a file or all video files in a directory and uploads them to [pastebin](https://pastebin.com/).

# Prerequisites
- [MediaInfo](https://mediaarea.net/en/MediaInfo/Download/Windows) in PATH.
- [pbwrap](https://github.com/Mikts/pbwrap) - Pastebin API wrapper for Python. Do `pip install pbwrap` to install.

# Usage
Add your pastebin credentials and API key in [`mediainfopaste.py`](https://github.com/Ravencentric/MediaInfo-Paste/blob/e42885b36a80ed6019673681033cbd301eceb5a7/mediainfopaste.py#L1-L3) before using it.

```cmd
C:\MediaInfo-Paste>mediainfopaste.py -h
usage: mediainfopaste.py [-h] [<path>]

Generates mediainfo and uploads to pastebin.

positional arguments:
  <path>      Path of the directory or file. Default: Current Working Directory.

options:
  -h, --help  show this help message and exit
```