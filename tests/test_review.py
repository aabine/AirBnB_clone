#!/usr/bin/python3
import unittest
from models.review import Review
from datetime import datetime

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        pass

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_attributes_defaults(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict_method(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(type(review_dict["created_at"]), str)
        self.assertEqual(type(review_dict["updated_at"]), str)
        self.assertTrue("__class__" in review_dict)
        
    def test_str_method(self):
        review_str = str(self.review)
        self.assertIn("[Review]", review_str)
        self.assertIn("'id':", review_str)
        self.assertIn("'created_at':", review_str)
        self.assertIn("'updated_at':", review_str)
        self.assertIn("'place_id':", review_str)
        self.assertIn("'user_id':", review_str)
        self.assertIn("'text':", review_str)
    
if __name__ == '__main__':
    unittest.main()
