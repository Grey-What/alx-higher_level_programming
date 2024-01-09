#!/usr/bin/python3
"""function replaces an element in a list at a
   specified index without modifing the orignal list"""


def new_in_list(my_list, idx, element):
    new_list = []
    for x in my_list:
        new_list.append(x)

    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
