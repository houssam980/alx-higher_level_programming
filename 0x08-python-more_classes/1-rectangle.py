#!/usr/bin/python3
"""Define Rectangle class
"""


class Rectangle:
    """Class Rectangle."""

    def __init__(self, width=0, height=0):
        """
        width : 0
        height : 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property width settings .(private)"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property height settings .(private)"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
