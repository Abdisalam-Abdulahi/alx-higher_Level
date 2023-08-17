#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {}
    for key, value in a_dictionary.items():
        value = value * 2
        new[key] = value
    return new
