#!/usr/bin/python3
"""Module that replaces elements in a list."""


def search_replace(my_list, search, replace):
    """Return a new list with every search element replaced by replace."""
    return [replace if item == search else item for item in my_list]
