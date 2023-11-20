#!/usr/bin/pytho3
def safe_print_list(my_list=[], x=0):
    idx = 0
    while my_list:
        try:
            if idx < x:
                print(my_list[idx], end="")
                idx += 1
            else:
                print()
                return idx
        except IndexError:
            print()
            return idx
