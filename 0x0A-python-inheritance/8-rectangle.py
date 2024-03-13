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
