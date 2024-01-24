#!/usr/bin/python3

"""Defines a class Square by size"""


class Square:
    """represents a square qith a size"""

    def __init__(self, size=0):
        """instantiation of square

        Args:
             size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """getter for private attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for private attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """determines area of square

        Returns: returns area of square
        """
        return (self.__size * self.__size)
