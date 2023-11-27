#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Define Rectangle"""

    num_inst = 0
    sym_print = "#"

    def __init__(self, width=0, height=0):
        """
        width : 0
        height : 0
        """
        self.width = width
        self.height = height
        type(self).num_inst += 1

    @property
    def width(self):
        """Getting property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        return self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter
        value :
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """representation
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.sym_print)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return rect

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        recten = "Rectangle(" + str(self.__width)
        recten += ", " + str(self.__height) + ")"
        return recten

    def __del__(self):
        """dropped Rectangle"""
        type(self).num_inst -= 1
        print("Bye rectangle...")
        
