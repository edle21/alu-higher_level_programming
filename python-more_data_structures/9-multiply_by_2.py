#!/usr/bin/python3
"""Module that multiplies all values of a dictionary by 2."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with every value of a_dictionary doubled."""
    return {key: value * 2 for key, value in a_dictionary.items()}
