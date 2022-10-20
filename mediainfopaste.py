username = "username"  # Pastebin username
password = "password"  # Pastebin password
api_key = "yourapikeyhere"  # Get this from here: https://pastebin.com/doc_api

import argparse
import os
import subprocess
from pathlib import Path

import pbwrap


def pastebin(file):
    mediainfo = subprocess.getoutput(["mediainfo", file])
    pb = pbwrap.Pastebin(api_key)
    token = pb.authenticate(username, password)
    url = pb.create_paste(
        api_paste_code=mediainfo,
        api_paste_private=0,
        api_paste_name=file,
        api_paste_expire_date=None,
        api_paste_format=None,
    )
    print(file, "-", url.replace("https://pastebin.com/", "https://pastebin.com/raw/"))


parser = argparse.ArgumentParser(
    description="Generates mediainfo and uploads to pastebin."
)
parser.add_argument(
    "path",
    nargs="?",
    metavar="<path>",
    type=Path,
    help="Path of the directory or file. Default: Current Working Directory.",
)
args = parser.parse_args()

if args.path == None:
    fullpath = os.getcwd()
    for file in os.listdir():
        if file.endswith(".mkv") or file.endswith(".mp4") or file.endswith(".m2ts"):
            pastebin(file)
    end = input("Press any key to exit...")

else:
    fullpath = str(args.path)
    if (
        fullpath.endswith(".mkv")
        or fullpath.endswith(".mp4")
        or fullpath.endswith(".m2ts")
    ):
        if "\\" in fullpath:
            directory = fullpath[0 : fullpath.rfind("\\")]
            file = fullpath[fullpath.rfind("\\") + 1 :]
            os.chdir(directory)
            pastebin(file)
        else:
            pastebin(fullpath)
    else:
        os.chdir(fullpath.rstrip('"'))
        for file in os.listdir():
            if file.endswith(".mkv") or file.endswith(".mp4") or file.endswith(".m2ts"):
                pastebin(file)
