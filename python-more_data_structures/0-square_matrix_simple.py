#!/usr/bin/python3
"""Module that squares every value of a matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with the square of each value of matrix."""
    return [[n ** 2 for n in row] for row in matrix]
