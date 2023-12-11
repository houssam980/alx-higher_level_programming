#!/usr/bin/python3
"""Defining Base class"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects

