#!/usr/bin/python3
''' validate size '''


class Square:
    '''add size feild to the square class'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        ''' Returns position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''set position to value '''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' returns the area of the square '''
        return self.__size * self.__size

    def my_print(self):
        ''' Print square using # '''
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for sp in range(0, self.__position[0]):
                    print(" ", end="")
                for idx in range(0, self.__size):
                    print("#", end="")
                print()
