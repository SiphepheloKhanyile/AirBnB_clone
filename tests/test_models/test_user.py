#!/usr/bin/python3
"""
User class test
"""
import unittest
from models import user
from models.base_model import BaseModel
User = user.User


class TestUser(unittest.TestCase):
    """User class Test"""
    def test_is_subclass(self):
        """Test User class instnatiation"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))


if __name__ == "__main__":
    unittest.main()
