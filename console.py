#!/usr/bin/python3
"""console module"""
import cmd
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
