#!/usr/bin/python3

'''
class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
'''


class BaseGeometry:
    '''
    Geometry class
    '''
    def area(self):
        ''' raise exception '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates value '''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    ''' Reactangel class '''

    def __init__(self, width, height):
        ''' initilaize arguments'''
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
