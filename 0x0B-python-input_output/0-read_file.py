#!/usr/bin/python3
"""openining File using with"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        """print file's stdout"""
        print(f.read(), end="")
