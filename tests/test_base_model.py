#!/usr/bin/env python3
"""
Module for testing the "BaseModel" class in "base_model" module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Testing Class for BaseModel Class
    """
    def setUp(self):
        self.base_model = BaseModel()

    def test_instance_attributes(self):
        """Test Instance attributes"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        """Ensure that the ID is a string"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        """Ensure that created_at is a datetime object"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        """Ensure that updated_at is a datetime object"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        """Testing save() method"""
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Testing to_dict() Method"""
        model_dict = self.base_model.to_dict()

        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_to_dict_datetime_format(self):
        """Testing to_dict datetime format"""
        model_dict = self.base_model.to_dict()
        created_at = datetime.strptime(model_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(model_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        self.assertEqual(created_at, self.base_model.created_at)
        self.assertEqual(updated_at, self.base_model.updated_at)


if __name__ == "__main__":
    unittest.main()
