#!/usr/bin/python3
"""Contains a Class Base with institiation function"""


class Base:
    """Base model for project

    represents a Base

    Private Class Attribute:
    __nb_objects (int): numbe rof instances of Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
