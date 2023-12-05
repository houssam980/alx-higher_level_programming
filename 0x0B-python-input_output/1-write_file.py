#!/usr/bin/python3
"""Define file overwriting"""


def write_file(filename="", text=""):
    """Print file's content to sdtout
    params :
        filename : file's name
        text : string written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
