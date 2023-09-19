#!/usr/bin/python3
'''
Geometry Module
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
