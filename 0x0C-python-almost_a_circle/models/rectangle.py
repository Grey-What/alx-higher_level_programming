#!/usr/bin/python3
"""Contain subclass Rectangle of Class Base"""
from models.base import Base


class Rectangle(Base):
    """represents an instance of Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of instance

        Args:
             width (int): width of instance
             height (int): height of instance
             x (int): co-ordinate
             y (int): co-ordinate
             id (int): identity of instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width of Rectangle Instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of attr width

        Args:
        value (int): value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of attr height

        Args:
        value (int): height of instance
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of attr x

        Args:
        value (int): value of x coordinate
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of attr y

        Args:
        value (int); value of y coordinate
        """
        if type(value) != int:
            raise TypeError("y must ba an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """determines area of instance of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout object represneted in '#'"""
        for y in range(0, self.__y):
            print("")

        for row in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for col in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """returns representation of instance in specified format"""
        rep_str = "[Rectangle] (" + str(self.id) + ") "
        rep_str += str(self.__x) + "/" + str(self.__y)
        rep_str += " - " + str(self.__width) + "/" + str(self.__height)
        return rep_str

    def update(self, *args, **kwargs):
        """updates instance attributes with arguments

        Args:
             *args (list); arguments to update attributes
             **kwargs (dict): attribute;value pairs of instance
        """
        if args and len(args) != 0:
            attr_list = ["id", "width", "height", "x", "y"]
            for attr, val in zip(attr_list, args):
                setattr(self, attr, val)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns dict representation of Rectangle"""
        return {
              "id": self.id,
              "size": self.width,
              "x": self.x,
              "y": self.y,
        }
