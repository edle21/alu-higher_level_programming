#!/usr/bin/python3
"""Module that squares every value of a matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with the square of each value of matrix."""
    new_matrix = []
    for row in matrix:
        new_row = []
        for number in row:
            new_row.append(number ** 2)
        new_matrix.append(new_row)
    return new_matrix
