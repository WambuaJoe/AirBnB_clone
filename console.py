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

    def do_emptyline(self):
        """does nothing when no command is passed to interpreter"""
        pass

    def help_emptyline(self):
        """help output for emptyline command"""
        print("No execution when nothing is entered")
        print()

    def do_EOF(self, line):
        """End-Of-File command to exit shell"""
        return True
        print()

    def help_EOF(self):
        """help output for the EOF cmd"""
        print("Exiting the shell when Ctrl+D is invoked")
        print()

    def do_quit(self, line):
        """quit command that exits the program"""
        return True
        print()

    def help_quit(self):
        """help output for the quit command"""
        print("Quit command that exits the program")
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
