#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    while True:
        try:
            if idx < x:
                print("{:d}".format(my_list[idx]), end='')
                idx += 1
            else:
                print()
        except (ValueError, TypeError):
            continue
