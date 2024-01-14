#!/usr/bin/env python3
"""
The HBNBCommand class is an entry point for an interpreter.
Allows users to interact with the program.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point class for the interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, line):  # pylint: disable=W0613
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):  # pylint: disable=invalid-name,W0613
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help for the quit/EOF commands"""
        print("".join(["Quit command to exit the program", "\n"]))

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
