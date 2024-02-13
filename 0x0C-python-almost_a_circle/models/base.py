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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation to file

        Args:
             cls (class); name of class
             list_objs (list): list of instances
        """
        filename = str(cls.__name__) + '.json'
        dict_list = []

        with open(filename, 'w') as open_file:
            if list_objs is None:
                json_str = "[]"
                open_file.write(json_str)
            else:
                for inst in list_objs:
                    obj_dict = cls.to_dictionary(inst)
                    dict_list.append(obj_dict)

                json_str = cls.to_json_string(dict_list)
                open_file.write(json_str)

    def from_json_string(json_string):
        """return the list of JSON string representation

        Args:
             json_string (json string): represents a list of dictionaries
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates instance of class with attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                my_inst = cls(1, 1)
            else:
                my_inst = cls(1)
            my_inst.update(**dictionary)
            return my_inst

    @classmethod
    def load_from_file(cls):
        """return list of instances from a json file"""
        filename = str(cls.__name__) + ".json"
        inst_list = []

        try:
            with open(filename, "r") as open_file:
                obj_list = Base.from_json_string(open_file.read())
                return [cls.create(**obj) for obj in obj_list]
        except IOError:
            return []
