#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
import unittest
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing the State class instantiation"""

    def test_class_instantiation(self):
        """
        Test for class instantiation
        """
        self.assertEqual(State, type(State()))


if __name__ == "__main__":
    unittest.main()
