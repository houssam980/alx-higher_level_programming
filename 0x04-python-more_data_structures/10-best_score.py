#!/usr/bin/python3
def best_score(a_dictionary):
    nw_score = 0
    for s in a_dictionary:
        if not s in a_dictionary:
            return None
        else:
            nw_score = max(a_dictionary, isinstance(a_dictionary[s]))
            return nw_score
