#!/usr/bin/env python3
"""
Module for testing file_storage module
"""
import unittest
import os
from models.base_model import BaseModel
from models import storage  # Import the storage instance for testing

class TestFileStorage(unittest.TestCase):
    """
    Test Class for `FileStorage` Class in `file_storage.py`
    """
    def setUp(self):
        self.file_path = storage._FileStorage__file_path # type: ignore
        self.objects = storage._FileStorage__objects # type: ignore
        self.base_model = BaseModel()
        self.key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """
        Testing `all()` method
        """
        all_objects = storage.all()
        self.assertEqual(all_objects, self.objects)

    def test_new_method(self):
        """
        Testing `new_method()`
        """
        storage.new(self.base_model)
        self.assertIn(self.key, self.objects)
        self.assertEqual(self.objects[self.key], self.base_model)

    def test_save_method(self):
        """
        Testing `save()` method
        """
        storage.new(self.base_model)
        storage.save()

        with open(self.file_path, 'r') as file:  # pylint: disable=W1514
            data = file.read()
            self.assertIn(self.base_model.id, data)

    def test_reload_method(self):
        """
        Testing `reload()` method
        """
        storage.new(self.base_model)
        storage.save()
        storage.reload()

        self.assertIn(self.key, self.objects)
        reloaded_object = self.objects[self.key]

        self.assertEqual(reloaded_object.id, self.base_model.id)
        self.assertEqual(reloaded_object.created_at, self.base_model.created_at)
        self.assertEqual(reloaded_object.updated_at, self.base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
