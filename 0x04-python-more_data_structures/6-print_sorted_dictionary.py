#!/usr/bin/python3
"""function prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    item_list = sorted(a_dictionary.items())
    for key, value in item_list:
        print(f"{key}: {value}")
