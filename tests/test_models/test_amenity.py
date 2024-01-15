#!/usr/bin/python3
"""
Defines unittests for models/amenity.py
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_instantiation(self):
        """
        Test for instantiation
        """
        self.assertEqual(Amenity, type(Amenity()))

    def test_attribute(self):
        """
        Test for attribute
        """
        self.assertIsInstance(Amenity.name, str)


if __name__ == "__main__":
    unittest.main()
