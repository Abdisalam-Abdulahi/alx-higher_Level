#!/usr/bin/python3

'''
function the returns the addition of two numbers
a and b must be integers or floats, otherwise raise a TypeError exception with
the message a must be an integer or b must be an integer
'''


def add_integer(a, b=98):
    '''
    add a and b
    '''
    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")

    elif isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")

    return int(a + b)
