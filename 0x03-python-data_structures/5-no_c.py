#!/usr/bin/python3
'''function that removes all characters c and C from a string'''


def no_c(my_string):
    new_string = my_string.translate({ord('c'): None})
    new_string = new_string.translate({ord('C'): None})
    return new_string
