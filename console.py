#!/usr/bin/python3
""" module console.py"""
import json
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models import storage
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """class hbnb console command"""
    prompt = "(hbnb) "
    lista_class = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]
    instance = None

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Exit command to exit the program"""
        return True

    def emptyline(self):
        """return a newline"""
        pass

    def do_create(self, line):
        """create a instance"""
        path_to_create = line + "()"
        if len(line) > 0:
            if line in HBNBCommand.lista_class:
                instance = eval(path_to_create)
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """show whith name a id"""
        string = line.split()
        all_objs = models.storage.all()
        if len(line) > 0:
            if string[0] in HBNBCommand.lista_class:
                if len(string) > 1:
                    key = string[0] + "." + string[1]
                    if key in all_objs:
                        print(all_objs[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """delete a instance in file json"""
        string = line.split(" ")
        if len(string[0]) == 0:
            print("** class name missing **")
        elif string[0] not in HBNBCommand.lista_class:
            print("** class doesn't exist **")
        elif len(string) == 1:
            print("** instance id missing **")
        else:
            all_objs = models.storage.all()
            key = string[0] + "." + string[1]
            if key in all_objs:
                all_objs.pop(key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """all the instances o a specific"""
        string = line.split()
        objs_list = []
        all_objs = models.storage.all()
        if len(line) != 0:
            if string[0] in HBNBCommand.lista_class:
                for k, v in all_objs.items():
                    if v.__class__.__name__ == string[0]:
                        objs_list.append(str(all_objs[k]))
                print(objs_list)
            else:
                print("** class doesn't exist **")
        else:
            for k, v in all_objs.items():
                objs_list.append(str(all_objs[k]))
            print(objs_list)

    def do_update(self, line):
        """update instance of all"""
        string1 = line.split()
        string = shlex.split(line)
        all_objs = models.storage.all()
        if len(string) < 1:
            print("** class name missing **")
        elif string[0] not in HBNBCommand.lista_class:
            print("** class doesn't exist **")
        elif len(string) < 2:
            print("** instance id missing **")
        elif len(string) < 3:
            print("** attribute name missing **")
        elif len(string) < 4:
            print("** value missing **")
        else:
            key = string[0] + "." + string[1]
            if key in all_objs:
                object1 = all_objs.get(key)
                word = string1[3]
                if string[3].isdigit() and word[0] is not '"':
                    setattr(object1, string[2], eval(string[3]))
                else:
                    setattr(object1, string[2], string[3])
                models.storage.save()
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
