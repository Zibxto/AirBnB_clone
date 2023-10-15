import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
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

    def test_default_values(self):
        """ Ensure that default attribute values are empty strings """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
