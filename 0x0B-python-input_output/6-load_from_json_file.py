#!/usr/bin/python3
"""contains function that creates python object from JSON file"""
import json


def load_from_json_file(filename):
    """decodes JSON file to python object

    Args:
         filename (str); name of JSON file
    """
    with open(filename, 'r') as op_file:
        return json.load(op_file)
