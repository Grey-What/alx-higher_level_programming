#!/usr/bin/python3
"""function returns a tuple with the legth
   of a string and it's first character"""


def multiple_returns(sentence):
    my_tuple = ()
    if len(sentence) == 0:
        my_tuple = (0, None)
    else:
        my_tuple = (len(sentence), sentence[0])
    return my_tuple
