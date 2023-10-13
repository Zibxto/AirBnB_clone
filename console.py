#!/usr/bin/python3
"""
Module for console
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = '(hbnb) '
    MODELS = {
        "BaseModel": BaseModel,
        "User": User
    }

    def default(self, line):
        if '.' not in line:
            super().default(line)
            return
        instance = line.split('.')
        classname = instance[0] if len(instance) > 0 else None
        _method = instance[1].split('(')[0] if len(instance) > 1 else None
        if _method:
            args = instance[1].split('(')[1][:-1]
        if classname in self.MODELS:
            if _method == 'all':
                self.do_all(classname)
        else:
            print("** class doesn't exist **")

    def do_create(self, model):
        """Creates a new instance of model
        """
        if model:
            if model in self.MODELS:
                new_model = self.MODELS[model]()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split(' ')
        if len(arg) < 1:
            print("** class name missing **")
            return
        model = args[0] if args[0] else None
        id = args[1] if len(args) > 1 else None

        if model:
            if model in self.MODELS:
                if id:
                    for obj_val in storage.all().values():
                        if id == obj_val.id:
                            print(obj_val)
                            return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split(' ')
        if len(arg) < 1:
            print("** class name missing **")
            return
        model = args[0] if args[0] else None
        id = args[1] if len(args) > 1 else None

        if model:
            if model in self.MODELS:
                if id:
                    for obj_key, obj_val in storage.all().items():
                        if id == obj_val.id:
                            del storage.all()[obj_key]
                            storage.save()
                            return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, model):
        """Prints all string representation of all instances
        based or not on the class name
        """
        models_list = []
        if model:
            if model not in self.MODELS:
                print("** class doesn't exist **")
                return

            for obj_val in storage.all().values():
                if obj_val.to_dict()['__class__'] == model:
                    models_list.append(obj_val.__str__())
            print(models_list)
        else:
            for obj_val in storage.all().values():
                models_list.append(obj_val.__str__())
            print(models_list)

    def do_update(self, line):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        """
        args = split_line(line)
        if len(line) < 1:
            print("** class name missing **")
            return
        model = args[0] if args[0] else None
        id = args[1] if len(args) > 1 else None
        attr_name = args[2] if len(args) > 2 else None
        attr_val = args[3] if len(args) > 3 else None

        if model:
            if model in self.MODELS:
                if id:
                    for obj_val in storage.all().values():
                        if id == obj_val.id:
                            if attr_name:
                                if attr_val:
                                    setattr(obj_val, attr_name, attr_val)
                                    obj_val.save()
                                    return
                                else:
                                    print("** value missing **")
                                    return
                            else:
                                print("** attribute name missing **")
                                return
                    print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

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


def split_line(line_string):
    output = []
    has_quote = False
    arg = ''
    for char in line_string:
        if char == ' ' and not has_quote:
            if arg:
                output.append(arg)
                arg = ''
        elif char == '"':
            has_quote = not has_quote
        else:
            arg += char
    if arg:
        output.append(arg)
    return output


if __name__ == '__main__':
    HBNBCommand().cmdloop()
