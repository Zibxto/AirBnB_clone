import unittest
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
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
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
