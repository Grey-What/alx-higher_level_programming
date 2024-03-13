#!/usr/bin/python3
"""contains function that writes an object to a text
   file, using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an python object to an text file using JSON rep

    Args:
         my_obj (python object): to write to text file
         filename (str): name  of file to write too
    """
    with open(filename, 'w') as op_file:
        json.dump(my_obj, op_file)
