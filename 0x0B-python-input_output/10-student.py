#!/usr/bin/python3
"""Class Student"""


class Student:
    """represents a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation of instance of student with
           first and laste name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation of instance

        Args:
             attrs (list): list of key names, else None
        """
        item_dict = self.__dict__
        attr_dict = {}

        if not isinstance(attrs, list):
            return item_dict
        for k in attrs:
            for item in item_dict:
                try:
                    attr_dict[k] = item_dict[k]
                except KeyError:
                    pass
        return attr_dict
