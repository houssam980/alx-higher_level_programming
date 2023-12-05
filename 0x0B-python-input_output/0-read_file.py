#!/usr/bin/python3
"""Define file reading"""


def read_file(filename=""):
    """Print file's content to sdtout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
