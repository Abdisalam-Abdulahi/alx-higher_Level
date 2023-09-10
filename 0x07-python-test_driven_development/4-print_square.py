#!/usr/bin/python3
'''
function that prints a square with the character #
'''


def print_square(size):
    '''
    print sqaure using #
    '''

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for k in range(size):
            print("#", end="")
        print()
