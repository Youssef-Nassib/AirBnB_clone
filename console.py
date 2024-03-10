#!/usr/bin/python3
"""console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """hbnbcommand class responsible on the cmd consol

    Attributes:
        prompt (str): command prompt.
    """

    prompt = "(hbnb) "

    def quit_cmd(self, arg):
        """function that quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """function that exit program when EOF is reached"""
        print("")
        return True

    def EmptyLine(self):
        """do nothing when empty line is inserted"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
