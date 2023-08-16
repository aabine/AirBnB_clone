#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_init_with_kwargs(self):
        data = {
            "id": "123",
            "created_at": "2023-01-01T00:00:00.000000",
            "updated_at": "2023-01-01T00:00:00.000000",
            "custom_attr": "value"
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, "123")
        self.assertEqual(instance.created_at, datetime(2023, 1, 1))
        self.assertEqual(instance.updated_at, datetime(2023, 1, 1))
        self.assertEqual(instance.custom_attr, "value")

    def test_save_updates_updated_at(self):
        instance = BaseModel()
        previous_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(previous_updated_at, instance.updated_at)

    def test_to_dict(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(instance_dict["created_at"],
                         instance.created_at.isoformat())
        self.assertEqual(instance_dict["updated_at"],
                         instance.updated_at.isoformat())
        self.assertEqual(instance_dict["__class__"], "BaseModel")


if __name__ == '__main__':
    unittest.main()
