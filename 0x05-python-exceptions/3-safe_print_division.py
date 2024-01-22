#!/usr/bin/python3
''' safe_print_division - divides two ints, handles exceptions '''


def safe_print_division(a, b):
    result = 0;
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
