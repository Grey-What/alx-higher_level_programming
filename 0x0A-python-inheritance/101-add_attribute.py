#!/usr/bin/python3
"""function that adds new attribute to an object if it is possible"""


def add_attribute(obj, attr, value):
    """adds new attribute to object if possible,
       else raise TypeError exception with cunstom message

    Args:
        obj (obj): instance to add attribute too
        attr (): attribute name to add
        value (): value of attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
