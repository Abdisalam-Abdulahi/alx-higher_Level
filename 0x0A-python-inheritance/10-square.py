#!/usr/bin/python3

'''
class Square that inherits from Reactangel
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square class '''

    def __init__(self, size):
        ''' initialize arguments '''
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        ''' calculate the area of the Square '''
        return self.__size * self.__size