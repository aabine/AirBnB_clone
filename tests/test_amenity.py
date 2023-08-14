#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        pass

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attributes_defaults(self):
        self.assertEqual(self.amenity.name, "")
        
    def test_to_dict_method(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(type(amenity_dict["created_at"]), str)
        self.assertEqual(type(amenity_dict["updated_at"]), str)
        self.assertTrue("__class__" in amenity_dict)
        
    def test_str_method(self):
        amenity_str = str(self.amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("'id':", amenity_str)
        self.assertIn("'created_at':", amenity_str)
        self.assertIn("'updated_at':", amenity_str)
        self.assertIn("'name':", amenity_str)
    
if __name__ == '__main__':
    unittest.main()
