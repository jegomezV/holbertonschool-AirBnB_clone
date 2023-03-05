#!/usr/bin/python3
"""Console module"""

import cmd
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    file = None
    classes =\
        ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, Line):
        """EOF command to exit the program"""
        return True

    def do_create(self, line):
        """create command creates a instance of the especified class
        """
        if not line:
            print("** class name missing **")
            return
        if line in HBNBCommand.classes:
            inst = eval(line)()
            inst.save()
            print(inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """show command prints the string representation of an instance
            based on the class name and id
        """
        words = line.split()
        if not line:
            print("** class name missing **")
            return
        if words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(words) < 2:
            print("** instance id missing **")
            return
        try:
            with open("file.json", "r") as file:
                dic = json.load(file)
            key = words[0] + "." + words[1]
            if key in dic:
                inst = eval(words[0])(**dic[key])
                print(inst)
            else:
                print("** no instance found **")
        except FileNotFoundError:
            print("** no instance found **")

    def do_destroy(self, line):
        """destroy command deletes an instance based on the class name and id
        """
        words = line.split()
        if not line:
            print("** class name missing **")
            return
        if words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(words) == 1:
            print("** instance id missing **")
            return
        obj = storage.all()
        key = words[0] + "." + words[1]
        if key in obj:
            del obj[key]
            storage.save()
        else:
            print("** no instance found **")


    def do_all(self, line):
        """Prints all string representation of all instances
            based or not on the class name
        """
        strs = []
        if line:
            words = line.split()
            if words[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        dic = storage.all()
        for key, value in dic.items():
            strs.append(str(value))
        print(strs)

    def emptyline(self):
        """empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
