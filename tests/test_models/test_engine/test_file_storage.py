import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


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

    def test_default_dict(self):
        """ Ensure that default dictionary is empty """
        obj = self.file_storage.all()
        self.assertEqual(obj, {})

    def test_object_added_count(self):
        """ Ensure that default dictionary is has key/values """
        for _ in range(3):
            BaseModel()
        obj = self.file_storage.all()
        self.assertEqual(len(obj), 3)

    def test_all_method(self):
        """ Ensure the all method returns a dictionary """
        all_objects = self.file_storage.all()
        self.assertTrue(isinstance(all_objects, dict))

    def test_new_method(self):
        """ Test the new method for adding objects """
        user_obj = User()
        self.file_storage.new(user_obj)

        # Check if the object is in the objects dictionary
        all_objects = self.file_storage.all()
        key = "{}.{}".format(user_obj.__class__.__name__, user_obj.id)
        self.assertTrue(key in all_objects)

        def test_save_method(self):
            """ Test the save method for serializing objects """
            user_obj = User()
            self.file_storage.new(user_obj)
            self.file_storage.save()

            # Check if the JSON file exists
            self.assertTrue(os.path.exists
                            (FileStorage._FileStorage__file_path))

        def test_reload_method(self):
            """ Test the reload method for deserializing objects """
            user_obj = User()
            self.file_storage.new(user_obj)
            self.file_storage.save()

            # Create a new instance of FileStorage and reload objects
            new_storage = FileStorage()
            new_storage.reload()

            # Check if the object is in the reloaded objects
            all_objects = new_storage.all()
            key = "{}.{}".format(user_obj.__class__.__name__, user_obj.id)
            self.assertTrue(key in all_objects)


if __name__ == '__main__':
    unittest.main()
