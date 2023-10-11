#!/usr/bin/python3
"""
Module for console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """Go to newline when ENTER is executed
        """
        pass

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
