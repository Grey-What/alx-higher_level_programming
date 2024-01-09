#!/usr/bin/python3
"""function finds all multiples of 2 in a list and creates new list
   that contains true or false depending on the condition checked"""


def divisible_by_2(my_list=[]):
    result_list = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list
