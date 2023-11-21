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
	   self.__size = size
        
	@property
        def size(self):
            """getting and setting"""
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """return the exact value of area by:
        size ** 2"""
        return self.__size ** 2
