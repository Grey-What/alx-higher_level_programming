#!/usr/bin/python3
"""contains function that appends text to the end of a file
   and returns number of characters added
"""


def append_write(filename="", text=""):
    """appends text to end of a file and return number of characters added

    Args:
         filename (str): file to added text to
         text (str); text to append to file
    """
    with open(filename, 'a', encoding="utf-8") as op_file:
        return (op_file.write(text))
