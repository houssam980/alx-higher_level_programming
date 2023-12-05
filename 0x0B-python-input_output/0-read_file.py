#!/usr/bin/python3
"""openining File using with"""


def read_file(filename=""):
    with open("filename", "r" ,encoding="UTF8") as f:
        """print file's stdout"""
        print(f.read(), end=")
