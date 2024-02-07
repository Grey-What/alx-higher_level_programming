#!/usr/bin/python3
"""contains function that writes a string to text file and returns number of char written"""


def write_file(filename="", text=""):
    """writes string to text file and return numbe rof characters written

    Args:
         filename (str): file to write too
         text (str): string to write to file
    """
    with open(filename, 'w', encoding="utf-8") as op_file:
        return (op_file.write(text))
