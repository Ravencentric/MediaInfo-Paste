import argparse
import os
import subprocess
from pathlib import Path

import pbwrap

# Pastebin username
USERNAME = "username"
# Pastebin password
PASSWORD = "password"
# Get this from here: https://pastebin.com/doc_api
API_KEY = "your_api_key_here"


class MediaInfoPaste:
    def __init__(self, args) -> None:
        def pastebin(file):
            """
            Accepts a file, generates the mediainfo, and
            uses pbwrap to upload it to pastebin.
            """
            mediainfo = subprocess.getoutput(["mediainfo", file])
            pb = pbwrap.Pastebin(API_KEY)
            pb.authenticate(USERNAME, PASSWORD)
            url = pb.create_paste(
                api_paste_code=mediainfo,
                api_paste_private=0,
                api_paste_name=file[:100],
                api_paste_expire_date=None,
                api_paste_format=None,
            )
            if args.r:
                url = url.replace(
                    "https://pastebin.com/",
                    "https://pastebin.com/raw/"
                )
            if args.md:
                print(f"[{file}]({url})")
            if args.bb:
                print(f"[url={url}]{file}[/url]")
            if args.md is False and args.bb is False:
                print(f"{file} - {url}")

        if Path.is_file(args.p):
            directory, file = os.path.split(Path.resolve(args.p))
            os.chdir(directory)
            pastebin(file)

        elif Path.is_dir(args.p):
            os.chdir(args.p)
            files = os.listdir()
            for file in files:
                if (
                    file.endswith(".mkv")
                    or file.endswith(".m2ts")
                    or file.endswith(".mp4")
                    or file.endswith(tuple(args.ex))
                ):
                    pastebin(file)
        else:
            print("Invalid Path")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generates MediaInfo and uploads it to pastebin."
    )
    parser.add_argument(
        "-p",
        metavar="<path>",
        type=Path,
        required=False,
        default=os.getcwd(),
        help="directory or file (default: current working directory)",
    )
    parser.add_argument(
        "-r",
        action="store_true",
        help="get raw pastebin links"
    )
    parser.add_argument(
        "-md",
        action="store_true",
        help="get markdown formatted output"
    )
    parser.add_argument(
        "-bb",
        action="store_true",
        help="get bbcode formatted output"
    )
    parser.add_argument(
        "-ex",
        metavar=".mkv .mp4",
        nargs="*",
        default="",
        help="additional extensions to look for in a given directory",
    )
    args = parser.parse_args()
    MediaInfoPaste(args)
