#!/usr/bin/python3
# function finds biggest integer in a list

def max_integer(my_list=[]):
    max_int = my_list[0]

    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if my_list[i] > max_int:
            max_int = my_list[i]
    return max_int
