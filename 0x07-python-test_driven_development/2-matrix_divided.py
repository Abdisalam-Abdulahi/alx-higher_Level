#!/usr/bin/python3

'''
a function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
    divides div to all matrix sub list elements
    '''
    new = []
    check = True

    if isinstance(div, int) is False or isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for liste in matrix:
        if isinstance(liste, list):
            for idx in range(len(matrix) - 1):
                if len(matrix[idx]) != len(matrix[idx + 1]):
                    check = False
                    break

            if check:  # if rows has the same size
                nArr = []
                for li in liste:
                    if isinstance(li, int) or isinstance(li, float):
                        numb = li / div
                        numb = round(numb, 2)
                        nArr.append(numb)
                    else:
                        raise TypeError("matrix must be a matrix "
                                        "(list of lists) of integers/floats")
                new.append(nArr)
            else:
                raise TypeError("Each row of the matrix must have the same "
                                "size")
        else:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
    return new
