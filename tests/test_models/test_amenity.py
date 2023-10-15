import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for this model""" 
    def test_default_values(self):
        """ Ensure that default attribute values are empty strings """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
