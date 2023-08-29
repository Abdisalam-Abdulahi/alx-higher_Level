#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = nuInts = 0
    while True:
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end="")
                i += 1
                nuInts += 1
            else:
                print()
                return nuInts
        except (ValueError, TypeError):
            i += 1
            continue
