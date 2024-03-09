#!/usr/bin/python3
"""define unittests for base_model.py in models

Unittest classes:
    test"""
import unittest
from base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):

    def test_init_with_no_args(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        created_at = "2024-03-09T12:00:00.000000"
        updated_at = "2024-03-09T13:00:00.000000"
        model = BaseModel(id="test_id", created_at=created_at, updated_at=updated_at)
        self.assertEqual(model.id, "test_id")
        self.assertEqual(model.created_at, datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model.updated_at, datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f"))

    def test_save_method(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict['__class__'], "BaseModel")
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_method(self):
        model = BaseModel()
        self.assertIsInstance(str(model), str)

if __name__ == '__main__':
    unittest.main()
