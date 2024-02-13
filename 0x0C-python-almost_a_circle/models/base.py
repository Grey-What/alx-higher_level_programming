#!/usr/bin/python3
"""Contains a Class Base with institiation function"""
import json


class Base:
    """Base model for project

    represents a Base

    Private Class Attribute:
    __nb_objects (int): numbe rof instances of Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns JSON string representation of object

        Args:
             list_dictionaries (list of dict): python object to encode
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
