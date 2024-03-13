#!/usr/bin/python3
"""Empty class BaseGeometry"""


class BaseGeometry:
    """represents a class"""

    def area(self):
        """raise exception that area is not implimented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
             name (str): name
             value (int): a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
