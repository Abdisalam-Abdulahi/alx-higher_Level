#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    maxi = 0
    i = 0
    for key, value in a_dictionary.items():
        i += 1
        if i == 1:
            maxi = value
        if value > maxi:
            maxi = value
    return list(a_dictionary.keys())[list(a_dictionary.values()).index(maxi)]
