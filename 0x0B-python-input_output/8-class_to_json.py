#!/usr/bin/python3
"""contains function that returns the dict
   description for JSON serialization
"""


def class_to_json(obj):
    """returns the dict representation of a data structure

    Args:
         obj (instance of a class): return __dict__
    """
    return obj.__dict__
