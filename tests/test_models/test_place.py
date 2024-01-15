#!/usr/bin/python3
"""Defines unittests for models/place.py.
"""
import unittest
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """testing instantiation of the Place class."""

    def test_instantiation(self):
        """Test for instantiation"""
        self.assertEqual(Place, type(Place()))


if __name__ == "__main__":
    unittest.main()
