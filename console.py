#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import re
from shlex import split

import models
from models.base_model import BaseModel

CLASSES = [
    "BaseModel",
]

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    """checks if args is valid

    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    args_list = parse(args)

    if len(args_list) == 0:
        print("** class name missing **")
    elif args_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return args_list


class HBNBCommand(cmd.Cmd):
    """The class that implements the console
    for the AirBnB clone web application
    """
    prompt = "(hbnb) "
    dbase = models.dbase

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def default(self, arg):
        """Default behaviour for cmd module when input is invalid"""
        action_map = {
            "all": self.hb_all,
            "show": self.hb_show,
            "destroy": self.hb_destroy,
            "count": self.hb_count,
            "update": self.hb_update,
            "create": self.hb_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)

            print("*** Unknown syntax: {}".format(arg))
            return False
        args_list = parse(arg)
        if len(args_list) == 0:
            print("** class name missing **")
            return False

        print("*** Unknown syntax: {}".format(arg))
        return False
    
    def hb_EOF(self, argv):
        """EOF signal to exit the program"""
        print("")
        return True

    def hb_quit(self, argv):
        """When executed, exits the console."""
        return True

    def hb_create(self, argv):
        """Creates a new instance of BaseModel, saves it (to a JSON file)
        and prints the id"""
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.dbase.save()

    def hb_show(self, argv):
        """Prints the string representation of an instance based
        on the class name and id"""
        args = check_args(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in self.dbase.all():
                    print("** no instance found **")
                else:
                    print(self.dbase.all()[key])

    def hb_all(self, argv):
        """Prints all string representation of all instances based or not
        based on the class name"""
        arg_list = split(argv)
        objects = self.dbase.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def hb_destroy(self, argv):
        """Delete a class instance based on the name and given id."""
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.dbase.all():
                    del self.dbase.all()[key]
                    self.dbase.save()
                else:
                    print("** no instance found **")

    def hb_update(self, argv):
        """Updates an instance based on the class name and id by adding or
        updating attribute and save it to the JSON file."""
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.dbase.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        object = self.dbase.all()[instance_id]
                        if arg_list[2] in type(object).__dict__:
                            v_type = type(object.__class__.__dict__[arg_list[2]])
                            setattr(object, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(object, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")

            self.dbase.save()

    def hb_count(self, arg):
        """Retrieve the number of instances of a class"""
        arg1 = parse(arg)
        count = 0
        for object in models.dbase.all().values():
            if arg1[0] == type(object).__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
