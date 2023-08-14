#!/usr/bin/python3
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def tearDown(self):
        pass

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_attributes_defaults(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_to_dict_method(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(type(city_dict["created_at"]), str)
        self.assertEqual(type(city_dict["updated_at"]), str)
        self.assertTrue("__class__" in city_dict)

    def test_str_method(self):
        city_str = str(self.city)
        self.assertIn("[City]", city_str)
        self.assertIn("'id':", city_str)
        self.assertIn("'created_at':", city_str)
        self.assertIn("'updated_at':", city_str)
        self.assertIn("'state_id':", city_str)
        self.assertIn("'name':", city_str)


if __name__ == '__main__':
    unittest.main()
