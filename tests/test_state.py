#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def tearDown(self):
        pass

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))

    def test_attributes_defaults(self):
        self.assertEqual(self.state.name, "")

    def test_to_dict_method(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(type(state_dict["created_at"]), str)
        self.assertEqual(type(state_dict["updated_at"]), str)
        self.assertTrue("__class__" in state_dict)
        
    def test_str_method(self):
        state_str = str(self.state)
        self.assertIn("[State]", state_str)
        self.assertIn("'id':", state_str)
        self.assertIn("'created_at':", state_str)
        self.assertIn("'updated_at':", state_str)
        self.assertIn("'name':", state_str)
    
if __name__ == '__main__':
    unittest.main()
