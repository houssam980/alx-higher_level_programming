#!/usr/bin/python3
"""converting string to pyhon datastru"""
import json


def from_json_string(my_str):
    """Python data structure) represented
       by a JSON string
    """
    return json.loads(my_str)
