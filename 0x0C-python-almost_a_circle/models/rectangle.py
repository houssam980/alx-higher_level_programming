#!/usr/bin/python3
"""Defining Rectangle that inherits from Base"""
from base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """rectangle width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        self.int_validations("width", value, False)
        self.__width = value


    @property
    def height(self):
        """rectangle height"""
        return self.__height
    

    @height.setter
    def height(self, value):
        self.int_validations("height", value, False)
        self.__height = value


    @property
    def x(self):
        """rect's x"""
        return self.__x
    

    @x.setter
    def x(self, value):
        self.int_validations("x", value)
        self.__x = value

    @property
    def y(self):
        """rect's y """
        return self.__y
    
    @y.setter
    def y(self, value):
        self.int_validations("y", value)
        self.__y = value


    def int_validations(value, attr_name):
        """int type validation method"""
        if type(value) not in int:
            raise TypeError("{} must be an integer".format(attr_name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr_name))
        

    def area(self):
        """area operation"""
        return self.width * self.height
    

    def display(self):
        """string reprisentation"""
        pr_st = "\n" * self.y + \
        (" " * self.x + "#" * self.width + "\n") * self.height
        print(pr_st, end="")

    def __str__(self):
        """Returns string infos"""
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)
    


    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """update instance attr"""
        if id != None:
            self.id = id
        if width != None:
            self.width = width
        if height != None:
            self.height = height
        if x != None:
            self.x = x
        if y != None:
            self.y = y
    
    def update(self, *args, **kwargs):
        """update instance attr from args and keyword args"""
        if args:
            self.__update(*args)
        else:
            self.__update(**kwargs)


    def to_dictionary(self):
        """return dict"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.x, "y": self.y}
