#!/usr/bin/python3
"""writing to a JSON file"""
import json


def save_to_json_file(my_obj, filename):
	"""writing object to a json file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
