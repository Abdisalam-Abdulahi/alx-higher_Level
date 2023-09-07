#!/usr/bin/python3
''' validate size '''


class Square:
    '''add size feild to the square class'''
    def __init__(self, size=0):
        self.__size = size
        if (isinstance(self.__size, int)) is False:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        ''' returns the area of the square '''
        return self.__size * self.__size
