#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
import json
import re


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program.
        """
        return True

    def do_EOF(self, arg):
        """Handles End Of File character.
        """
        print()
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
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
        """Prints the string representation of an instance.
        """
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
        """Deletes an instance based on the class name and id.
        """
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
        """Prints all string representation of all instances.
        """
        if arg != "":
            string = arg.split(' ')
            if string[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for k, obj in storage.all().items()
                      if type(obj).__name__ == string[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, arg)
        clsname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
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
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[clsname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[k], attribute, value)
                storage.all()[k].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
