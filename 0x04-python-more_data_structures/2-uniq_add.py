#!/usr/bin/python3
"""function adds all the unique integers in a list"""


def uniq_add(my_list=[]):
    new_set = set(my_list)
    new_list = list(new_set)
    result = 0

    for n in new_list:
        result += n
    return result
