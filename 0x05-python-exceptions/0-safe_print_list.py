#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ix = 0
    while True:
        try:
            if ix < x:
                print(my_list[ix], end='')
                ix += 1
            else:
                print()
                return ix
        except IndexError:
            print()
            return ix
