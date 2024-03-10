#!/usr/bin/python3
"""unitest moduls for file storage0"""
import unittest
import os
from file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create a sample object to use in tests
        self.sample_object = {"id": 1, "name": "Test Object"}

        # Initialize FileStorage and add the sample object
        self.storage = FileStorage()
        self.storage.new(self.sample_object)

    def tearDown(self):
        # Remove the file created during tests
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method(self):
        # Test if all() method returns correct dictionary
        self.assertEqual(self.storage.all(), {"dict": {"id.1": self.sample_object}})

    def test_save_and_reload_methods(self):
        # Test save() and reload() methods
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(new_storage.all(), {"dict": {"id.1": self.sample_object}})

if __name__ == '__main__':
    unittest.main()
