import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for this model"""
    def setUp(self):
        """
        Initialize class instance
        """
        self.file_storage = FileStorage()

    def tearDown(self):
        """
        Remove class instance
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """ Ensure that default dictionary is empty """
        obj = self.file_storage.all()
        self.assertEqual(obj, {})

    def test_object_added_count(self):
        """ Ensure that default dictionary is has key/values """
        for _ in range(3):
            BaseModel()
        obj = self.file_storage.all()
        self.assertEqual(len(obj), 3)

if __name__ == '__main__':
    unittest.main()
