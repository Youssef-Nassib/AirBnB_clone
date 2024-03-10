#!/usr/bin/python3
"""console module"""
import cmd
from models.base_model import BaseModel
import re


class HBNBCommand(cmd.Cmd):
    """hbnbcommand class responsible on the cmd consol

    Attributes:
        prompt (str): command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """function that exit program when EOF is reached"""
        print("")
        return True

    def emptyline(self):
        """does nothing when empty line is inserted"""
        pass

    def so_creat(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints string representation of instance based on class name and id"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()
