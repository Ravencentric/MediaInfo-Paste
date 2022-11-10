# MediaInfo-Paste
Generates the mediainfo of a file or all video files in a given directory and uploads them to [pastebin](https://pastebin.com/).

# Prerequisites
- [MediaInfo](https://mediaarea.net/en/MediaInfo/Download/Windows) in PATH.
- [pbwrap](https://github.com/Mikts/pbwrap) - Pastebin API wrapper for Python. Do `pip install pbwrap` to install.

# Usage
Add your pastebin credentials and API key in [`mediainfopaste.py`](https://github.com/Ravencentric/MediaInfo-Paste/blob/main/mediainfopaste.py#L9-L14) before using it.

```
> mediainfopaste.py --help
usage: mediainfopaste.py [-h] [-p <path>] [-r] [-md] [-bb] [-ex [.mkv .mp4 ...]]

Generates MediaInfo and uploads it to pastebin.

options:
  -h, --help           show this help message and exit
  -p <path>            directory or file (default: current working directory)
  -r                   get raw pastebin links
  -md                  get markdown formatted output
  -bb                  get bbcode formatted output
  -ex [.mkv .mp4 ...]  additional extensions to look for in a given directory
```