#!/usr/bin/python3
"""Define checker of a class"""


def is_same_class(obj, a_class):
    """checking if it the same
    params :
       obj : object
       a_class: specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
