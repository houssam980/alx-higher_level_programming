#!/usr/bin/python3
for i in range(0, 99 + 1):
    if i < 99:
        print("{:02}".format(i), end=", ")
else:
    print("{:02}".format(i))
