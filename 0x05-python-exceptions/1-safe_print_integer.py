#!/usr/bin/python3
""" safe_print_integer - prints an integer and handle exception"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
