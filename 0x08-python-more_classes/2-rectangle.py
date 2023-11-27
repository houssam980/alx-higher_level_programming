#!/usr/bin/python3
"""Rectangle Class."""


class Rectangle:
    """define Rectangle."""

    def __init__(self, width=0, height=0):
        """
        width: 0
        height: 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property setting and getting with return"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setting"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property setting and getting with return"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return printed 
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for iterate in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if iterate != self.__height - 1:
                rect.append("\n")
        return rect

