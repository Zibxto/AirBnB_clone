import unittest
from models.state import State

class TestUserModel(unittest.TestCase):
    def test_default_values(self):
        """ Ensure that default attribute values are empty strings """
        state = State()
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
