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
        self.size = size

    @property
    def size(self):
        """getting and setting"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return the exact value of area by:
        size ** 2"""
        return self.__size ** 2


    def my_print(self):
        """print square ini sdtout with # char"""
        if self.__size > 0 and self.__size < 0:
            for iterate in range (self.__size):
                for iterate_2 in range(self.__size):
                    print("#", end="")
        else:
            print()
