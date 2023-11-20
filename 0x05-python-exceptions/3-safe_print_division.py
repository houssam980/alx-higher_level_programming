#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        rest = a / b
        return rest
    except ZeroDivisionError:
        rest = None
        return rest
    finally:
        print("Inside result: {}".format(rest))
