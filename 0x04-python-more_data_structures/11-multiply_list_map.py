#!/usr/bin/python3
'''returns a list with all values multiplied
 by a number without using a loop'''


def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda a: a * number, my_list))
    return new_list
