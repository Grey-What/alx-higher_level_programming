#!/usr/bin/python3

"""a string in uppercase"""


def uppercase(str):
    for lett in str:
        if ord(lett) >= 97 and ord(lett) <= 122:
            lett = chr(ord(lett) - 32)
        print("{}".format(lett), end="")
    print("")
