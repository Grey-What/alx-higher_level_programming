#!/usr/bin/python3
"""Contains function that reads txt files"""


def read_file(filename=""):
    """Read text files (UTF8) and print to stdout

    Args:
         filename (str): name of file to read
    """
    with open(filename, 'r', encoding="utf-8") as open_file:
        print(open_file.read(), end="")
