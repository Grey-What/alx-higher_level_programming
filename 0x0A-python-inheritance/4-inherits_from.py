#!/usr/bin/python3
"""check if object is an instance of a class
   that inherited from another class
"""


def inherits_from(obj, a_class):
    """check if object is an instance
    of a class that is a subclass of another

    Args:
         obj: instance of class
         a_class: the parent class of class that instance obj is of
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
