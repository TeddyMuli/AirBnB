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

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    storage = models.Storage
    def do_quit(self, arg):
        """Exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True
    
    def emptyline(self):
        """Do nothing"""
        pass

    def help_quit(self):
        """Prints the help message for quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Prints the help message for EOF"""
        print("Quit command to exit the program")

    def create(self, arg):
        """Creates a new instance of 
        BaseModel and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in models.BaseModel:
            print("** class doesn't exist **")
        else:
            new = models.BaseModel[arg]()
            new.save()
            print(new.id)

    def show(self, arg):
        """Prints the string 
        representation of an 
        instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.BaseModel:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            inst_id = args[1]
            inst = BaseModel.get(args[0], inst_id)
            if inst is None:
                print("** no instance found **")
            else:
                print(inst)
            

if __name__ == 'main':
    HBNBCommand().cmdloop()

