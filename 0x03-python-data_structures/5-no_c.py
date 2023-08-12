#!/usr/bin/python3

def no_c(my_string):
    new = ''
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            letter = ''
        new += letter
    return new
