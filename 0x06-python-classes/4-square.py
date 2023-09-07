#!/usr/bin/python3
''' validate size '''


class Square:
    '''add size feild to the square class'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        ''' Returns size'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' set size to value '''
        if (isinstance(self.__size, int)) is False\
                or (isinstance(value, int)) is False:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        ''' returns the area of the square '''
        return self.__size * self.__size
