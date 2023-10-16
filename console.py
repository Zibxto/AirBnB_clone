#!/usr/bin/python3
"""
Module for console
"""
import cmd
import sys
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = '(hbnb) ' if sys.stdin.isatty() else '(hbnb) \n'
    MODELS = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    ERRORS = {
        "class_missing": "** class name missing **",
        "class_not_exist": "** class doesn't exist **",
        "no_instance_found": "** no instance found **",
        "instance_id_missing": "** instance id missing **",
        "attr_name_missing": "** attribute name missing **",
        "value_missing": "** value missing **",
    }

    def default(self, line):
        if '.' not in line:
            super().default(line)
            return

        if ')' != line[-1] or '(' not in line:
            super().default(line)
            return

        parts = re.split(r'\.|\(|\)', line)
        parts = [part.strip("' ") for part in parts if part.strip()]

        classname = parts[0] if len(parts) > 0 else None
        method = parts[1] if len(parts) > 1 else None
        args = parts[2] if len(parts) > 2 else None

        if args and '{' not in args and '}' != args[-1]:
            args = [arg.strip().strip('"') for arg in args.split(',')]
        elif args:
            args = [arg.strip().strip('"')for arg in args.split(",", 1)]

        if not method:
            super().default(line)
            return

        if classname in self.MODELS:
            if method == 'all':
                self.do_all(classname)
                return
            elif method == 'count':
                count = 0
                for obj_val in storage.all().values():
                    if obj_val.to_dict()['__class__'] == classname:
                        count += 1
                print(count)
                return
            elif method == 'show':
                id = args[0]
                line = "{} {}".format(classname, id)
                self.do_show(line)
                return
            elif method == 'destroy':
                id = args[0]
                line = "{} {}".format(classname, id)
                self.do_destroy(line)
                return
            elif method == 'update':
                if len(args) > 2:
                    id = args[0]
                    an = args[1]
                    av = args[2]
                    line = "{} {} {} {}".format(classname, id, an, av)
                    self.do_update(line)
                else:
                    id = args[0]
                    data = json.loads(args[1].replace("'", '"').strip())
                    for an, av in data.items():
                        line = "{} {} {} {}".format(classname, id, an, av)
                        self.do_update(line)
                return
        super().default(line)

    def do_create(self, model):
        """Creates a new instance of model
        """
        if not model:
            print(self.ERRORS["class_missing"])
            return
        if model in self.MODELS:
            new_model = self.MODELS[model]()
            new_model.save()
            print(new_model.id)
        else:
            print(self.ERRORS["class_not_exist"])

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split(' ')
        if len(arg) < 1:
            print(self.ERRORS["class_missing"])
            return
        model = args[0] if args[0] else None
        id = args[1] if len(args) > 1 else None

        if not model:
            print(self.ERRORS["class_missing"])
            return
        if model in self.MODELS:
            if not id:
                print(self.ERRORS["instance_id_missing"])
                return
            model_id = "{}.{}".format(model, id)
            for obj_key, obj_val in storage.all().items():
                if model_id == obj_key:
                    print(obj_val)
                    return
            print(self.ERRORS["no_instance_found"])
        else:
            print(self.ERRORS["class_not_exist"])

    def do_destroy(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split(' ')
        if len(arg) < 1:
            print(self.ERRORS["class_missing"])
            return
        model = args[0] if args[0] else None
        id = args[1] if len(args) > 1 else None

        if not model:
            print(self.ERRORS["class_missing"])
            return

        if model in self.MODELS:
            if not id:
                print(self.ERRORS["instance_id_missing"])
                return
            model_id = "{}.{}".format(model, id)
            for obj_key in storage.all().keys():
                if model_id == obj_key:
                    del storage.all()[obj_key]
                    storage.save()
                    return
            print(self.ERRORS["no_instance_found"])
        else:
            print(self.ERRORS["class_not_exist"])

    def do_all(self, model):
        """Prints all string representation of all instances
        based or not on the class name
        """
        models_list = []
        if model:
            if model not in self.MODELS:
                print(self.ERRORS["class_not_exist"])
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

        if not model:
            print(self.ERRORS["class_missing"])
            return

        if model in self.MODELS:
            if not id:
                print(self.ERRORS["instance_id_missing"])
                return
            model_list = [k for k in storage.all().keys()]
            model_id = "{}.{}".format(model, id)

            if model_id not in model_list:
                print(self.ERRORS["no_instance_found"])
                return

            for obj_val in storage.all().values():
                if not attr_name:
                    print(self.ERRORS["attr_name_missing"])
                    return

                if not attr_val:
                    print(self.ERRORS["value_missing"])
                    return

                if attr_val.isnumeric():
                    attr_val = int(attr_val)

                if id == obj_val.id:
                    setattr(obj_val, attr_name, attr_val)
                    obj_val.save()
                    return
        else:
            print(self.ERRORS["class_not_exist"])

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
    """Split line string into words in array
    """
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
