#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda lis: list(map(lambda i: i ** 2, lis)), matrix))
