#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for lis in matrix:
        new.append(list(map(lambda x: x ** 2, lis)))
    return (new)
