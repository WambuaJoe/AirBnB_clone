#!/usr/bin/python3
"""Console Module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command that exits the program"""
        return True

    def do_EOF(self, args):
        """EOF signal that exits the program when Ctrl-D is invoked"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
