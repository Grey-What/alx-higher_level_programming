#!/usr/bin/python3

""" safe_print_list - prints all specified elements of a list """


def safe_print_list(my_list=[], x=0):
    retval = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
            retval = retval + 1
        except IndexError:
                  break
        print("")
        return (ret_val)
