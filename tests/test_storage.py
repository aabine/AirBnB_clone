#!/usr/bin/python3
import unittest
import json
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_init(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        class MockObj:
            def __init__(self, id):
                self.id = id
        obj = MockObj("123")
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {"MockObj.123": obj})

    def test_save(self):
        class MockObj:
            def __init__(self, id):
                self.id = id
            def to_dict(self):
                return {"id": self.id}
        obj = MockObj("123")
        self.storage.new(obj)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as j_file:
            data = json.load(j_file)
            self.assertEqual(data, {"MockObj.123": {"id": "123"}})

    def test_reload(self):
        with open(self.storage._FileStorage__file_path, "w") as j_file:
            json.dump({"MockObj.456": {"id": "456"}}, j_file)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)
        self.assertEqual(self.storage.all()["MockObj.456"].id, "456")

if __name__ == '__main__':
    unittest.main()
