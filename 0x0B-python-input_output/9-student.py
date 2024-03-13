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

    def to_json(self):
        """return dictionary representation of instance"""
        return self.__dict__
