#!/usr/bin/python3
'''
create simple Reactangle
'''


class Rectangle:
    '''
    define a reactangle
    '''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        ''' returns width of the reactangel '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' set width to value '''
        if type(self.__width) is not int or type(value) is not int:
            raise TypeError("width must be an integer")

        elif self.__width < 0 or value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' returns heigtht of the reactangel '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' set height to value '''
        if type(self.__height) is not int or type(value) is not int:
            raise TypeError("height must be an integer")

        elif self.__height < 0 or value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
