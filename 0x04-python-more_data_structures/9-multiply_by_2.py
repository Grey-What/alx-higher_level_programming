#!/usr/bin/python3
'''function returns a new dictionary with all values multiplied by 2'''


def multiply_by_2(a_dictionary):
    new_dict = dict()

    for key, value in a_dictionary.items():
        new_dict.update({key: value * 2})
    return new_dict
