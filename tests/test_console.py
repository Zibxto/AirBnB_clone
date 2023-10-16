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

    def test_EOF(self):
        """ Ensure that EOF is present"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue().strip()
        self.assertEqual(output, "Quit command to exit the program")

    def test_empty_line(self):
        """ Ensure that line is empty"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

    def test_create_and_show_model(self):
        """ Ensure that model is created"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        self.assertTrue(id)
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(id))
            output = f.getvalue().strip()
        self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()
