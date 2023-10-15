import unittest
import os
import json
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
        all_objects = self.file_storage.all()
        key = "{}.{}".format(user_obj.__class__.__name__, user_obj.id)
        self.assertTrue(key in all_objects)

    def test_save_method(self):
        """ Test the save method for serializing objects """
        user_obj = User()
        self.file_storage.new(user_obj)
        self.file_storage.save()
        self.assertTrue(os.path.exists
                        (FileStorage._FileStorage__file_path))

    def test_reload_method(self):
        """ Test the reload method for deserializing objects """
        user_obj = User()
        self.file_storage.new(user_obj)
        self.file_storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        key = "{}.{}".format(user_obj.__class__.__name__, user_obj.id)
        self.assertTrue(key in all_objects)

    def test_reload_without_exception(self):
        """ Test that no exception is returned if file.json is not present """
        try:
            self.file_storage.reload()
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")

    def test_object_saved_to_file_json(self):
        """ Test if object created is saved in file.json"""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        obj.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            file_obj = json.loads(f.read())
            self.assertTrue(key in file_obj)

    def test_file_json_present(self):
        """ Test file.json is present when object instance is saved"""
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_new_method_sets_object_in_objects(self):
        """ Test setting objects in storage"""
        class MockObject:
            id = 1
            def to_dict(self):
                return {"__class__": "MockObject"}
        mock_obj = MockObject()
        self.file_storage.new(mock_obj)
        key = "MockObject.1"
        self.assertIn(key, self.file_storage.all())

    def test_reload_method_deserializes_json_file(self):
        """ Test number of objexts after reload"""
        BaseModel().save()
        BaseModel().save()
        self.file_storage.reload()
        self.assertEqual(len(self.file_storage.all()), 2)   

    def test_reload_method_with_nonexistent_file(self):
        """ Test reload method when file.json is not present"""
        try:
            self.file_storage.reload()
        except FileNotFoundError:
            self.fail("FileNotFoundError raised unexpectedly.")

    def test_class_attributes(self):
        """ Test that class attributes are correct"""
        self.assertIsInstance(self.file_storage._FileStorage__file_path, str)
        self.assertIsInstance(self.file_storage._FileStorage__objects, dict)
        # self.assertIsInstance(_objs, dict)

if __name__ == '__main__':
    unittest.main()
