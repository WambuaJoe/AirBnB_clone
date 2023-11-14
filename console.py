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

    def emptyline(self):
        """overwrite emptyline method"""
        return False

    def do_create(self, args):
        """create class instance & save to JSON file"""
        pass

    def do_show(self, args):
        """print string representation of instance based on
        class name & id
        """
        pass

    def do_destroy(self, args):
        """delete instance & save change to JSON file"""
        pass

    def do_all(self, args):
        """print string representation of all instances based on
        or not on the same class
        """
        pass

    def do_update(self, args):
        """update instance & save change to JSON file"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
