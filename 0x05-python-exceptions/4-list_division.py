#!/usr/bin/python3
""" diveds element by element in 2 list"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except TypeError:
            ans = 0
            print("wrong type")
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
        except IndexError:
            ans = 0
            print("out of range")
        finally:
            new_list.append(ans)
    return (new_list)
