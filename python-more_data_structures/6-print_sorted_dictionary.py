#!/usr/bin/python3
"""Module that prints a dictionary sorted by its keys."""


def print_sorted_dictionary(a_dictionary):
    """Print each key and value of a_dictionary, ordered by key."""
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
