#!/usr/bin/python3
"""function returns a key with the biggest integer value"""


def best_score(a_dictionary):
    if a_dictionary:
        score = 0
        winner = ''
        my_list = a_dictionary.keys()

        for key in my_list:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
                winner = key
        return winner
