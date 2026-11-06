#!/usr/bin/python3
"""Module that safely prints elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of my_list and return the number printed."""
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
