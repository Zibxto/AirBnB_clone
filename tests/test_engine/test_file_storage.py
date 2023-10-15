import unittest
from models.engine.file_storage import FileStorage

class TestUserModel(unittest.TestCase):
    def test_all(self):
        """ Ensure that default dictionary is empty """
        obj = FileStorage().all()
        self.assertEqual(obj, {})

if __name__ == '__main__':
    unittest.main()
