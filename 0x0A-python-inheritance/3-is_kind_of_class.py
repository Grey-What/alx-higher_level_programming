#!/usr/bin/python3
"""check if an object is an instance of
   or if the object is an instance of a class that
   inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """return the result of isintance

    Args:
         obj: object to check
         a_class; class and it's parents to compare obj too
    """
    return (isinstance(obj, a_class))
