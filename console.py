#!/usr/bin/python3
"""console madules"""
import cmd
import json
import os
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = 'file.json'

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            cls_name = args[0]
            id = args[1]
            with open(self.file, 'r') as f:
                data = json.load(f)
                key = "{}.{}".format(cls_name, id)
                if key in data:
                    print(data[key])
                else:
                    print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            cls_name = args[0]
            id = args[1]
            with open(self.file, 'r') as f:
                data = json.load(f)
            key = "{}.{}".format(cls_name, id)
            if key in data:
                del data[key]
                with open(self.file, 'w') as f:
                    json.dump(data, f)
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        objs = []
        if arg:
            try:
                cls_name = eval(arg).__name__
                with open(self.file, 'r') as f:
                    data = json.load(f)
                for key in data:
                    if cls_name in key:
                        objs.append(str(data[key]))
                print(objs)
                return
            except NameError:
                print("** class doesn't exist **")
                return
        with open(self.file, 'r') as f:
            data = json.load(f)
            for key in data:
                objs.append(str(data[key]))
        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            cls_name = args[0]
            id = args[1]
            attribute = args[2]
            value = args[3]
            with open(self.file, 'r') as f:
                data = json.load(f)
            key = "{}.{}".format(cls_name, id)
            if key not in data:
                print("** no instance found **")
                return
            obj = data[key]
            setattr(obj, attribute, value)
            obj.save()
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
        except KeyError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
