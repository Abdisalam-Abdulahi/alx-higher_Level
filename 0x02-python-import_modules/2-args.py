#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)

    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("{} argument:".format(n - 1))
        print("{}: {}".format(1, sys.argv[n - 1]))
    else:

        print("{} arguments:".format(n - 1))
        i = 1
        while (i < n):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
