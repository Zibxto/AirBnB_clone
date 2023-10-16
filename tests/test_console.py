from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Test cases for this model"""
    def test_quit(self):
        """ Ensure that quit method is present"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue().strip()
        self.assertEqual(output, "Quit command to exit the program")

if __name__ == '__main__':
    unittest.main()
