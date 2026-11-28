#!/usr/bin/python3
"""Unittests for the validation of Rectangle attributes."""
import unittest
from models.rectangle import Rectangle


class TestRectangleValidation(unittest.TestCase):
    """Tests for the Rectangle setters."""

    def test_not_integer(self):
        """Every attribute rejects values that are not integers."""
        r = Rectangle(10, 2)
        for name in ("width", "height", "x", "y"):
            for value in ("2", 1.5, None, {}, True):
                msg = "{} must be an integer".format(name)
                with self.assertRaisesRegex(TypeError, msg):
                    setattr(r, name, value)

    def test_size_not_positive(self):
        """width and height must be greater than 0."""
        r = Rectangle(10, 2)
        for name in ("width", "height"):
            for value in (0, -10):
                msg = "{} must be > 0".format(name)
                with self.assertRaisesRegex(ValueError, msg):
                    setattr(r, name, value)

    def test_negative_position(self):
        """x and y must not be negative."""
        r = Rectangle(10, 2)
        for name in ("x", "y"):
            msg = "{} must be >= 0".format(name)
            with self.assertRaisesRegex(ValueError, msg):
                setattr(r, name, -1)

    def test_constructor_validates(self):
        """The constructor uses the same validation."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)


if __name__ == "__main__":
    unittest.main()
