#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
import json
import re


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter

    Attributes:
        prompt (str): The command prompt
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Handles End Of File character"""
        print()
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            ob = storage.classes()[arg]()
            ob.save()
            print(ob.id)

    def do_show(self, arg):
        """Prints string representation of instance based on class name and id """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            string = arg.split(' ')
            if string[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(string) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(string[0], string[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[k])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            string = arg.split(' ')
            if string[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(string) < 2:
                print("** instance id missing **")
            else:
                k = "{}.{}".format(string[0], string[1])
                if k not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[k]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg != "":
            string = arg.split(' ')
            if string[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                doc = [str(obj) for k, obj in storage.all().items()
                      if type(obj).__name__ == string[0]]
                print(doc)
        else:
            str_list = [str(obj) for key, obj in storage.all().items()]
            print(str_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute"""
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, arg)
        clsname = match.group(1)
        uid = match.group(2)
        attb = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif clsname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(clsname, uid)
            if k not in storage.all():
                print("** no instance found **")
            elif not attb:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                typ = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        typ = float
                    else:
                        typ = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[clsname]
                if attb in attributes:
                    value = attributes[attb](value)
                elif typ:
                    try:
                        value = typ(value)
                    except ValueError:
                        pass
                setattr(storage.all()[k], attb, value)
                storage.all()[k].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
