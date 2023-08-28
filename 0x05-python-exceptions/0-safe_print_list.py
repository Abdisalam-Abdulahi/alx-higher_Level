#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new = my_list[:x]
    i = 0
    for li in new:
        print(li, end="")
        i += 1
    if x != 0:
        print()
    return i


try:
    safe_print_list()
except NameError:
    safe_print_list
