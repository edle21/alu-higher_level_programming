#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_inherits_from_base(self):
        """A rectangle is a Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_attributes(self):
        """The arguments go to the right attributes."""
        r = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (10, 2, 3, 4, 12))

    def test_default_position(self):
        """x and y are 0 by default."""
        r = Rectangle(10, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_id_increments(self):
        """Ids are assigned by Base."""
        first = Rectangle(10, 2)
        second = Rectangle(2, 10)
        self.assertEqual(second.id, first.id + 1)

    def test_setters(self):
        """Each setter changes its attribute."""
        r = Rectangle(1, 1)
        r.width, r.height, r.x, r.y = 5, 6, 7, 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))

    def test_attributes_are_private(self):
        """The private attributes cannot be reached."""
        r = Rectangle(1, 1)
        for name in ("__width", "__height", "__x", "__y"):
            self.assertFalse(hasattr(r, name))

    def test_missing_arguments(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle(1)


if __name__ == "__main__":
    unittest.main()
