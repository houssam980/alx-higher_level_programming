#!/usr/bin/python3
"""Define file appending"""


def append_write(filename="", text=""):
    """Print file's content to sdtout
    params :
        filename : file's name
        text : string appending
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
