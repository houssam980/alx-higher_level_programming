#!/usr/bin/python3
"""Define checker of a class"""


def is_kind_of_class(obj, a_class):
    """checking obj if instance of a_class
    params:
       obj : object
       a_class : class
       return True if instance
       otherwise False
    """
    if isinstance(obj(a_class)):
        return True
    else:
        return False
