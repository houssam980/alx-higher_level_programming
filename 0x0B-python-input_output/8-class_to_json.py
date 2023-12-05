"""dictionary description with simple data structure"""


def class_to_json(obj):
    """return dict for a class"""
    return obj.__dict__
