#!/usr/bin/python3
"""Contains function that reads txt files"""


def read_file(filename=""):
    """Read text files (UTF8) and print to stdout

    Args:
         filename (str): name of file to read
    """
    with open(filename, 'r') as open_file:
        file_read = open_file.read()
        print(file_read)
