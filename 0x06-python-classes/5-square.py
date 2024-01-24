#!/usr/bin/python3

"""Defines a class Square with private attribute size"""


class Square:
    """represents a square with a size"""

    def __init__(self, size=0):
        """instantiation of square instances

        Args:
             size (int): size of new square instance
        """
        self.size = size

    @property
    def size(self):
        """setter of private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for private attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square to stdout with # symbols"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
