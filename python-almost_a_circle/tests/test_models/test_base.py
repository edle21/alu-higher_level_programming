#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_is_assigned(self):
        """An instance without an id gets an integer id."""
        self.assertIsInstance(Base().id, int)

    def test_id_increments(self):
        """Each new id is the previous one plus 1."""
        first = Base()
        second = Base()
        self.assertEqual(second.id, first.id + 1)

    def test_given_id(self):
        """A given id is used as it is."""
        self.assertEqual(Base(12).id, 12)

    def test_zero_id(self):
        """Zero is a valid given id."""
        self.assertEqual(Base(0).id, 0)

    def test_given_id_does_not_count(self):
        """A given id does not increment the counter."""
        first = Base()
        Base(50)
        self.assertEqual(Base().id, first.id + 1)

    def test_counter_is_private(self):
        """The counter cannot be reached from outside."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects


if __name__ == "__main__":
    unittest.main()
