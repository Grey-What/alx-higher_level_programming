#!/usr/bin/python3
"""mostfunction returns the list of available
   attributes and methods of an object
"""


def lookup(obj):
    """returns properties of a class"""
    return (list(dir(obj)))
