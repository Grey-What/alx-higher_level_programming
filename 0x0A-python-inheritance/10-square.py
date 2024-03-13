#!/usr/bin/python3
"""inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents an instance of a square"""
    def __init__(self, size):
        """instantiation of instance

        Args:
             size (int): private positive int
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
