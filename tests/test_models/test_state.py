import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for this model"""
    def test_default_values(self):
        """ Ensure that default attribute values are empty strings """
        state = State()
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
