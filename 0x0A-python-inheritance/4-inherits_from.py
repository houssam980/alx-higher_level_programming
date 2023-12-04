#!/usr/bin/python3
"""define checking if onject instance of
   a class that inherited
 """


def inherits_from(obj, a_class):
    """
    params :
    obj : object
    a_class : class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
