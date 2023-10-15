import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for this model""" 
    def test_all(self):
        """ Ensure that default dictionary is empty """
        obj = FileStorage().all()
        self.assertEqual({}, {})

if __name__ == '__main__':
    unittest.main()
