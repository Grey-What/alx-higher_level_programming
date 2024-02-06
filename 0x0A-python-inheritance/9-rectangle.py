#!/usr/bin/python3
"""inherits from baseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from superclass"""
    def __init__(self, width, height):
        """instantiation of object"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of instance of Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """implimenting the print and str of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
