#!/usr/bin/python3

"""Defines a Class Square by size"""


class Square:
    """Represents a square with a size"""

    def __init__(self, size=0):
        """instantiation of instance

        Args:
             size (int): size of represented square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
