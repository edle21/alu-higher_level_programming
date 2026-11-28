#!/usr/bin/python3
"""
5-text_indentation module.

Provides a function that indents a text.
"""


def text_indentation(text):
    """Print text with 2 new lines after each ., ? and : character.

    Printed lines have no space at the beginning or at the end."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for mark in ".?:":
        text = text.replace(mark, mark + "\n\n")
    lines = [line.strip(" ") for line in text.split("\n")]
    print("\n".join(lines), end="")
