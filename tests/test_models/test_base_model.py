import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
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
        string = "[{}] ({}) {}".format(inst.__class__.__name__, id1, inst.__dict__)
        self.assertEqual(inst.__str__(), string)

if __name__ == '__main__':
    unittest.main()