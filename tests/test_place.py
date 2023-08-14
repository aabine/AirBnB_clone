#!/usr/bin/python3
import unittest
from models.place import Place
from datetime import datetime

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        pass

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_attributes_defaults(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        
    def test_to_dict_method(self):
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(type(place_dict["created_at"]), str)
        self.assertEqual(type(place_dict["updated_at"]), str)
        self.assertTrue("__class__" in place_dict)
        
    def test_str_method(self):
        place_str = str(self.place)
        self.assertIn("[Place]", place_str)
        self.assertIn("'id':", place_str)
        self.assertIn("'created_at':", place_str)
        self.assertIn("'updated_at':", place_str)
        self.assertIn("'city_id':", place_str)
        self.assertIn("'user_id':", place_str)
        self.assertIn("'name':", place_str)
        self.assertIn("'description':", place_str)
        self.assertIn("'number_rooms':", place_str)
        self.assertIn("'number_bathrooms':", place_str)
        self.assertIn("'max_guest':", place_str)
        self.assertIn("'price_by_night':", place_str)
        self.assertIn("'latitude':", place_str)
        self.assertIn("'longitude':", place_str)
        self.assertIn("'amenity_ids':", place_str)
    
if __name__ == '__main__':
    unittest.main()
