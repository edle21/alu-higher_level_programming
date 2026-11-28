#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_max_at_end(self):
        """The max is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """The max is in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The max is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_negative(self):
        """One negative number in the list."""
        self.assertEqual(max_integer([1, -2, 3]), 3)

    def test_all_negative(self):
        """Only negative numbers."""
        self.assertEqual(max_integer([-4, -1, -3]), -1)

    def test_one_element(self):
        """A list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument returns None."""
        self.assertIsNone(max_integer())

    def test_duplicates(self):
        """The max appears more than once."""
        self.assertEqual(max_integer([5, 5, 2]), 5)

    def test_floats(self):
        """Floats mixed with integers."""
        self.assertEqual(max_integer([1.5, 3.7, 2]), 3.7)

    def test_string(self):
        """A string returns its highest character."""
        self.assertEqual(max_integer("abc"), "c")

    def test_mixed_types(self):
        """Comparing a string with an integer fails."""
        with self.assertRaises(TypeError):
            max_integer([1, "2"])

    def test_none(self):
        """None has no length."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
