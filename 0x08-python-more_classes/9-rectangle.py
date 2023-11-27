#!/usr/bin/python3

"""Define Class"""


class Rectangle:
    """
    Rectangle Class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Define Rectangle
        width : 0
        height : 0
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """getting width"""
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
        """getting height and setting it."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return Rectangle with bigger Area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        return new rectangle
        cls:
        size: 0
        """
        return (cls(size, size))

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return printable representation
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for iterate in range(self.__height):
            [rect.append(str(self.print_symbol)) for lp_1 in range(self.__width)]
            if iterate != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return string"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Print Bye Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
