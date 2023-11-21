#!/usr/bin/python3
"""Square Module based on 0-square.py task"""


class Square:
    """class That Defines a Square"""
    def __init__(self, size=0):
        """method to be excuted
           with defult self param
           and size
           raising errors:
           TypeError : if size != 0
           ValueError : if size less than 0
        """
        if size != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the exact vlue of area by
        size ** 2"""
        return self.__size ** 2
