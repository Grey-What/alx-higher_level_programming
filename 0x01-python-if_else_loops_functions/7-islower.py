#!/usr/bin/python3
"""module check for a lowercase character"""


def islower(c):
    """check for lowercase character

    Args:
         c: value to check
    """

    if ord(c) >= 97 and ord(c) <= 122:
        return (True)
    else:
        return (False)
