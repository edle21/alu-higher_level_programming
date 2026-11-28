#!/usr/bin/python3
"""Unittests for Rectangle.area."""
import unittest
from models.rectangle import Rectangle


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method."""

    def test_area(self):
        """The area is width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_after_change(self):
        """The area follows the new size."""
        r = Rectangle(3, 2)
        r.width = 5
        self.assertEqual(r.area(), 10)

    def test_area_takes_no_argument(self):
        """area does not accept arguments."""
        with self.assertRaises(TypeError):
            Rectangle(3, 2).area(1)


if __name__ == "__main__":
    unittest.main()
