#!/usr/bin/python3
"""Defines a function that returns the JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (a string).

    Args:
        my_obj: The object to serialize.

    Returns:
        The JSON string representing my_obj.
    """
    return json.dumps(my_obj)
