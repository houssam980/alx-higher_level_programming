#!/usr/bin/python3
"""Defining Base class """
from json import dumps


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """costractor __init__"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """to json str"""
        if list_dictionaries == None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

