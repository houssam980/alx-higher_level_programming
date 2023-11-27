#!/usr/bin/python3
"""
Rectangle class.
"""


class Rectangle:
    """define rectangle"""

    def __init__(self, width=0, height=0):
        """
            width: 0
            height: 1
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Return printable string representation"""
        if self.__height == 0 or self.__width == 0:
            return ""
        recten_str = ""
        for iterate in range(self.__height):
            for lp_2 in range(self.__width):
                recten_str += "#"
            recten_str += "\n"
        return recten_str[:-1]

    def __repr__(self):
        """Return string representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
            value: value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height ."""
        return self.__height

    @height.setter
    def height(self, value):
        """
            value: value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area
        Return area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter
        Return Perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__width + self.__height

    def __del__(self):
        """print bye when dropped"""
        print("Bye rectangle...")

