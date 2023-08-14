#!/usr/bin/python3
import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        pass

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes_defaults(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict_method(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)
        self.assertTrue("__class__" in user_dict)
        
    def test_str_method(self):
        user_str = str(self.user)
        self.assertIn("[User]", user_str)
        self.assertIn("'id':", user_str)
        self.assertIn("'created_at':", user_str)
        self.assertIn("'updated_at':", user_str)
        self.assertIn("'email':", user_str)
        self.assertIn("'password':", user_str)
        self.assertIn("'first_name':", user_str)
        self.assertIn("'last_name':", user_str)
    
if __name__ == '__main__':
    unittest.main()
