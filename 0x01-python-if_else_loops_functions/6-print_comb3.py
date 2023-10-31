#!/usr/bin/python3
for i in range(0, 9):
    for a in range(i + 1, 10):
        if i == 8:
            print("{}{}".format(i, a))
        else:
            print("{}{}".format(i, a), end=", ")
