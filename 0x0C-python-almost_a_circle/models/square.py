#!/usr/bin/python3
"""Defining square that inherits from Rectangle"""


from rectangle import Rectangle


class square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self, size, x, y, id=None)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.x, self.width)

    
    @property
    def size(self):
        """square width"""
        return self.width
    
    @size.getter
    def size(self, value):
        self.width = value
        self.height = value

        
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
