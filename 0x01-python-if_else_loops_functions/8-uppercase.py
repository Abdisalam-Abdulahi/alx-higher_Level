#!/usr/bin/python3


def uppercase(str):
    new = ""
    for s in str:
        j = ord(s) - 32
        if 97 <= ord(s) <= 122:
            new += chr(j)
        else:
            new += s

    print(new)
