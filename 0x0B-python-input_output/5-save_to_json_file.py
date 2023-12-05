#!/usr/bin/python3
"""writing to json file"""
import json


def save_to_json_file(my_obj, filename):
    """Writing object to json file using dump"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
