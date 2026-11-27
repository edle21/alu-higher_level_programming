#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.

    Creates the file if it doesn't exist and overwrites it if it does.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
