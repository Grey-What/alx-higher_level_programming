#!/usr/bin/python3


def print_last_digit(number):
    """print laste digit of a number"""
    digit = abs(number) % 10

    print("{:d}".format(digit), end="")
    return (digit)
