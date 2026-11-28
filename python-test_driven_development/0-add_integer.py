#!/usr/bin/python3
"""
0-add_integer module.

Provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """Add two integers and return the result.

    Floats are cast to integers first; other types raise TypeError."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
