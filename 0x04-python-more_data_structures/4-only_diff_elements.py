#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff = []
    for elem in set_1:
        if elem in set_2:
            continue
        else:
            diff.append(elem)
    for item in set_2:
        if item in set_1:
            continue
        else:
            diff.append(item)

    return diff
