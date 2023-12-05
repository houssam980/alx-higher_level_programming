#!/usr/bin/python3
"""representation of json object"""
import json


def to_json_string(my_obj):
    """return json object"""
    return json.dump(my_obj)
