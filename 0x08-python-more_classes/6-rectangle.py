#!/usr/bin/python3
"""Defining my rectangle class"""


class Rectangle:
    """Define Rectangle"""

    num_instan = 0

    def __init__(self, width=0, height=0):
        """
        width : 0
        height : 0
        """
        self.width = width
        self.height = height
        type(self).num_instan += 1

    @property
    def width(self):
        """Get width"""
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
        """Height getting"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setting
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """String rep
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectn = []
        for iterate in range(self.__height):
            [rectn.append('#') for lp_1 in range(self.__width)]
            if iterate != self.__height - 1:
                rectn.append("\n")
        return "".join(rectn)

    def __repr__(self):
        """Return string"""
        rectn = "Rectangle(" + str(self.__width)
        rectn += ", " + str(self.__height) + ")"
        return rectn

    def __del__(self):
        """delete with bye msg"""
        type(self).num_instan -= 1
        print("Bye rectangle...")
