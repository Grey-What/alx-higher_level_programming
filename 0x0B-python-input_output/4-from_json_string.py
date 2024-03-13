#!/usr/bin/python3
"""contains function to decode JSON string to python object"""


def from_json_string(my_str):
    """decodes JSON string and return python object

    Args:
         my_str (JSON string): to be decoded to python object
    """
    import json
    return (json.loads(my_str))
