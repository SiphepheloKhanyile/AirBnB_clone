#!/usr/bin/env python3
"""
The HBNBCommand class is an entry point for an interpreter.
Allows users to interact with the program.
"""
from ast import mod
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Entry point class for the interpreter
    """
    p_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
    csob = [BaseModel]  # [User, State, City, Amenity, Place, Review]
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

    def do_create(self, cls_name):
        """
        Creates a new instance of `BaseModel`
        Saves it (to the `JSON` file) and prints the `id`
        Ex: `$ create BaseModel`
        """
        if cls_name == '':
            print("** class name missing **")
            return
        if cls_name not in self.p_classes:
            print("** class doesn't exist **")
        ob = self.csob[HBNBCommand.p_classes.index(cls_name)]()
        models.storage.save()
        print(ob.id)

    def do_show(self, cls_id : str):
        """
        Prints the string representation of an instance based on the `class name` and `id`.
        Ex: `$ show BaseModel 1234-1234-1234.`
        """
        path = 'file.json'
        o_dict = {}
        args = cls_id.split(' ')

        if len(args) == 1:
            if args[0] == '':
                print("** class name missing **")
            elif args[0] not in HBNBCommand.p_classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif args[0] not in HBNBCommand.p_classes:
            print("** class doesn't exist **")
        else:
            o_dict = models.storage.all()
            keyx = args[0] + '.' + args[1]
            if keyx in o_dict:
                print(o_dict[keyx])
            else:
                print("** no instance found **")

    def do_destroy(self, cls_id: str):
        """
        Deletes an instance based on:
        the `class name` and `id` (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`
        """
        args =cls_id.split(' ')
        if len(args) == 1:
            if args[0] == '':
                print("** class name missing **")
            elif args[0] not in HBNBCommand.p_classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif args[0] not in HBNBCommand.p_classes:
            print("** class doesn't exist **")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, cls_id: str):
        """
        Prints all string representation of all instances based or not on:
        the `class name`. 
        Ex: `$ all BaseModel or $ all`. 
        """
        lst = []
        args = cls_id.split(" ")
        if args[0]:
            if args[0] not in HBNBCommand.p_classes:
                print("** class doesn't exist **")
            else:
                for k in models.storage.all().keys(): \
                    # pylint: disable=C0201
                    if k.split('.')[0] == args[0]:
                        lst.append(models.storage.all()[k])
        else:
            for k in models.storage.all().keys(): \
                # pylint: disable=C0201
                lst.append(models.storage.all()[k])

        if lst:
            print([item.__str__() for item in lst]) \
                # pylint: disable=C2801
        lst.clear()

    def do_update(self, cls_id: str):
        """
        Updates an instance based on the:
        `class name` and `id` by adding or updating attribute
        (save the change into the JSON file).
        Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`. 
        Usage:
        `update <class name> <id> <attribute name> "<attribute value>"`
        """
        args = cls_id.split(' ')
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in HBNBCommand.p_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_k = args[0] + "." + args[1]
            obj_dict = models.storage.all()
            if isinstance(obj_k[3], int):
                obj_dict[obj_k][args[2]] = int(args[3])
                obj_dict[obj_k][args[2]] = \
                    int(obj_dict[obj_k][args[2]]) + 2
            else:
                args[3] = args[3].strip("'")
                setattr(obj_dict[obj_k], args[2], args[3].strip('"'))
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
