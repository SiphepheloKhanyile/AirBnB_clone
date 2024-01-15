#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import unittest
from models.city import City


class TestCity_ins(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_instantiation(self):
        """Testing instantiation"""
        self.assertEqual(City, type(City()))


if __name__ == "__main__":
    unittest.main()
