import unittest
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
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
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
