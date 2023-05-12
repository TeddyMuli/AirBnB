#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import re
from shlex import split

import models
from models.base_model import BaseModel

#Write a program called console.py that contains the entry point of the command interpreter:
#You must use the module cmd
#Your class definition must be: class HBNBCommand(cmd.Cmd):
#Your command interpreter should implement:
#quit and EOF to exit the program
#help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
#a custom prompt: (hbnb)
#an empty line + ENTER shouldn’t execute anything
#Your code should not be executed when imported

#Your code should be able to import the hbnb module
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

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

