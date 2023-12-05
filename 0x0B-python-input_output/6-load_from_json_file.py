#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """reading from json"""
    with open(filename) as f:
        json.load(f)
