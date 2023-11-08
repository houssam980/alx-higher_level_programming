#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    srt_list = sorted(a_dictionary.keys())
    for key in srt_list:
        print("{:s}: {}".format(key, a_dictionary[key]))
