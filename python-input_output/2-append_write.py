#!/usr/bin/python3
"""Defines a text file-appending function."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file.

    Creates the file if it doesn't exist.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
