#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_mtrx = matrix.copy()

    for val in range(len(matrix)):
        n_mtrx[val] = list(map(lambda x: x**2, matrix[val]))

    return (n_mtrx)
