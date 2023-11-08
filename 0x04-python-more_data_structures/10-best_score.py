#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    big_score = max(a_dictionary.values())
    for key, va in a_dictionary.items():
        if va == big_score:
            return key
