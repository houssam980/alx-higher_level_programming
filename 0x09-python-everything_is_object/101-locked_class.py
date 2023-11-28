#!/usr/bin/python3
"""
Defining class
"""


class LockedClass:
    """
    prevent the user from dynamically creating new instance...
    """
    __slots__ = ["first_name"]
