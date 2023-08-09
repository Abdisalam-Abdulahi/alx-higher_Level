#!/usr/bin/python3

def print_last_digit(number):
    num_str = repr(number)
    last_digit = num_str[-1]
    last_digit = int(last_digit)
    return last_digit
