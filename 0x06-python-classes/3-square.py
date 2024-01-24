#!/usr/bin/python3

"""Defines a class Square by size"""


class Square:
    """represents a square qith a size"""

    def __init__(self, size=0):
        """instantiation of square

        Args:
             size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """determines area of square

        Returns: returns area of square
        """
        return (self.__size * self.__size)
