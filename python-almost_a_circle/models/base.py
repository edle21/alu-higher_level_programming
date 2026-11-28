#!/usr/bin/python3
"""Module that defines the Base class."""


class Base:
    """Base class that manages the id of all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance.

        Args:
            id (int): identity of the instance, assigned automatically
                if None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
