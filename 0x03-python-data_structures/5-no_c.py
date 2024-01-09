#!/usr/bin/env python3
# function that removes all characters c and C from a string

def no_c(my_string):
    new_string = ''
    for chr in my_string:
        if chr != 'c' and chr != 'C':
            new_string = new_string + chr
    return new_string
