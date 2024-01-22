#!/usr/bin/python3
""" safe_print_list_integers - prints first x integer elements of list """


def safe_print_list_integers(my_list=[], x=0):
    ret = 0;

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
