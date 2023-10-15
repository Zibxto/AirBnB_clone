import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for this model"""
    def test_default_values(self):
        """ Ensure that default attribute values are empty strings """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
