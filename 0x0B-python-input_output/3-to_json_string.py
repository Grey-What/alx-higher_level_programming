#!/usr/bin/python3
"""module contains function that returns JSON rep of an object(string)"""


def to_json_string(my_obj):
    """return JSON representation of object

    Args:
         my_obj (str): python object to encode to JSON
    """
    import json
    return (json.dumps(my_obj))
