import unittest
from models import storage

class TestFileStorage(unittest.TestCase):
    """Test cases for this model""" 
    def test_all(self):
        """ Ensure that default dictionary is empty """
        obj = storage.all()
        self.assertEqual({}, {})

if __name__ == '__main__':
    unittest.main()
