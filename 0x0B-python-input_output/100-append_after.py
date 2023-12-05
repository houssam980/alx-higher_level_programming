#!/usr/bin/python3
"""Define insertion content"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text

    params:
        filename : file name
        search_string : string will search
        new_string: insert string
    """

    conte = ""
    with open(filename) as fr:
        for ln in fr:
            conte += ln
            if search_string in ln:
                conte += new_string
    with open(filename, "w") as fw:
        fw.write(conte)
