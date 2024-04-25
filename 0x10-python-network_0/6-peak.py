#!/usr/bin/python3
"""
find a peak in a list of integers
"""


def find_peak(list_of_integers):
    """
    determines peak in data

    Args:
    list_of_integers (list): list of vlaues tov determine peak of
    Returns: peak in values, else None
    """
    size = len(list_of_integers)
    effective_mid = size
    peak = size // 2

    if size == 0:
        return None

    while True:
        effective_mid = effective_mid // 2
        if (peak < size - 1 and
                list_of_integers[peak] < list_of_integers[peak + 1]):
            if effective_mid // 2 == 0:
                effective_mid = 2
            peak = peak + effective_mid // 2
        elif (effective_mid > 0
              and list_of_integers[peak] < list_of_integers[peak - 1]):
            if effective_mid // 1 == 0:
                effective_mid = 2
            peak = peak - effective_mid // 2
        else:
            return list_of_integers[peak]
