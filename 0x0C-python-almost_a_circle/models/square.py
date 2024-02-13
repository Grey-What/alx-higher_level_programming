#!/usr/bin/python3
"""declaration of a Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square Instance"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instatiation instance of square

        Args:
             size (int): Size of the Square
             x (int): x coordinate of Square
             y (int): y coordinate of square
             id (int); identity of Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for instance attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for intstance attribute size

        Args:
             value (int): size of size of Square
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates instance attributes

        Args:
             args (list): list of attribute values
             kwargs (dict): attribute name and values
        """
        attr_list = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for attr, val in zip(attr_list, args):
                setattr(self, attr, val)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """return instance of Square in specified format"""
        return ("[square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))
