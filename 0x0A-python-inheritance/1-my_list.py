#!/usr/bin/python3
'''
class MyList that inherits from list
'''


class MyList(list):
    '''
    class that prints list in ascending order
    '''
    def print_sorted(self):
        '''
        return sorted list
        '''
        print(sorted(self))
