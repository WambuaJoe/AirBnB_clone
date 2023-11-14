#!/usr/bin/python3
"""Console module"""
import cmd
import time


class HBNBCommand(cmd.Cmd):
    """HBNB console class"""
    timestamp = time.time()
    current = time.ctime(timestamp)
    msg = f"HBNB console ({current})\n\
Type 'help' or ? to show more details\n"
    intro = f"{msg}"
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit command that exits the program"""
        print("Quitting...")
        return True

    def do_EOF(self, line):
        """exit shell by pressing Ctrl+D"""
        print("Exiting the shell...")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
