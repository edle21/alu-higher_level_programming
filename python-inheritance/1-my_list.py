
#!/usr/bin/python3
"""Define a custom list class."""


class MyList(list):
    """A list with a method to print sorted elements."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))

