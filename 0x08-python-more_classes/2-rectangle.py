#!/usr/bin/python3
""" empty class Rectangle"""


class Rectangle:
    """represents a rectangl"""

    def __init__(self, width=0, height=0):
        """initialises instance of Rectangle

        Args:
            width (int): private attribute representing width of rectangle
            height (int): private attribute representing height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retreives value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """determines area of instance of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """determines perimeter of instance of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
