import unittest
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Test cases for this model"""
    def setUp(self):
        """
        Initialize class instance
        """
        self.file_storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Remove class instance
        """
        FileStorage._FileStorage__objects = {}

    def test_id_uniqueness(self):
        """
        Test that 'id' values are unique.
        """
        id1 = BaseModel().id
        id2 = BaseModel().id
        self.assertNotEqual(id1, id2)

    def test_instance_uniqueness(self):
        """
        Test that instances are unique.
        """
        inst = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst, inst2)

    def test_id_is_string(self):
        """
        Test that the id is a string
        """
        id1 = BaseModel().id
        self.assertIsInstance(id1, str)

    def test_model_is_instance_class(self):
        """
        Test that the model is an instance of BaseModel
        """
        inst = BaseModel()
        self.assertIsInstance(inst, BaseModel)

    def test_instance_str(self):
        """
        Test that the instance print string representation
        """
        inst = BaseModel()
        id1 = inst.id
        string = "[{}] ({}) {}".format(inst.__class__.__name__,
                                       id1, inst.__dict__)
        self.assertEqual(inst.__str__(), string)

    def test_init_method_with_no_arguments(self):
        """
        Test initialization of BaseModel without arguments
        """
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_init_method_with_arguments(self):
        """
        Test initialization of BaseModel with arguments
        """
        test_id = str(uuid.uuid4())
        kwargs = {
            "id": test_id,
            "created_at": "2023-10-15T12:00:00.000000",
            "updated_at": "2023-10-15T12:00:00.000000",
            "att": "value"
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, test_id)

    def test_save_method_updates_updated_at(self):
        """
        Test if the save method updates the updated_at attribute
        """
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict_method_returns_dictionary(self):
        """
        Test if the to_dict method returns a dictionary
        """
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)

    def test_str_method_returns_string_representation(self):
        """
        Test if the __str__ method returns a string representation
        """
        string_representation = str(self.base_model)
        self.assertIsInstance(string_representation, str)

if __name__ == '__main__':
    unittest.main()
