#!/usr/bin/python3
"""check if a object is an instance of specified class"""


def is_same_class(obj, a_class):
    """return result of isinstance

    Args:
         obj - object to check instance of
         a_class - class to check
    """
    return (type(obj) == a_class)
