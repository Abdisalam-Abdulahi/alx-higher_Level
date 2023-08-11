#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    result = 0
    i = 1
    while i < n:
        result += int(sys.argv[i])
        i += 1
    print(result)
