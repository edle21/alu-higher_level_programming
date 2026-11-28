#!/usr/bin/python3
"""
4-print_square module.

Provides a function that prints a square.
"""


def print_square(size):
    """Print a square of side size with the character #.

    size must be an integer greater than or equal to 0."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
