#!/usr/bin/python3
"""Defines a function that returns the dictionary description of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are all serializable
            (list, dictionary, string, integer or boolean).

    Returns:
        The dictionary of the object's attributes.
    """
    return obj.__dict__
