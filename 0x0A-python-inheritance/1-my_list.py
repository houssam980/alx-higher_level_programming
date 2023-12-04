#!/usr/bin/python3
"""define Mylist Class"""


class MyList(list):
    """print sorted list"""

    def print_sorted(self):
        print(sorted(self))
