#!/usr/bin/python3

"""Defines a class Square with private attribute size"""


class Square:
    """represents a square with a size"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiation of square instances

        Args:
             size (int): size of new square instance
             position (tuple): tuple of two positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter of private attribute position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter for private attribute position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square to stdout with # symbols"""
        if self.__size == 0:
            print("")

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            [print("")]
