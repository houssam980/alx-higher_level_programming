#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    idx = ints_to_print= 0
    while True:
        try:
            if idx < x:
                print("{:d}".format(my_list[idx]), end='')
                idx += 1
                ints_to_print += 1
            else:
                print()
                return ints_to_print
        except (ValueError, TypeError):
            idx += 1
