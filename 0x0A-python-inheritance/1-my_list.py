#!/usr/bin/python3
"""Define MyList Class"""


class MyList(list):
    """child class"""
    def __init__(self):
        """invoke constractor from parents class"""
        super().__init__(self)
    def print_sorted(self):
        """print list in sorted"""
        print(sorted(self))
