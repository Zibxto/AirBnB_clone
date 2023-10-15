import unittest
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
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
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
