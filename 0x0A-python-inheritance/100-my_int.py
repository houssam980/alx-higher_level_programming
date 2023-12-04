#!/usr/bin/python3
"""define MyInt class inherited from int"""


class MyInt(int):
    """class defining as a rebel"""
    def __eq__(self, n):
        """operators inverted  = != !="""
        return super().__ne__(n)
    def __ne__(self, n):
        """operators inverted  != == ="""
        return super().__eq__(n)

