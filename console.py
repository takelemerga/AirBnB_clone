#!/usr/bin/python3
"""console module"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

"""this is a module that contains the entry point of
   the command interpreter
"""


class HBNBCommand(cmd.Cmd):
    """ a class that implement cmd command """

    cmd.Cmd.prompt = "(hbnb) "
    name_classes = {"BaseModel": BaseModel, "User": User,
                    "Place": Place, "State": State, "City": City,
                    "Amenity": Amenity, "Review": Review}

    def do_quit(self, line):
        """Quit command to exit the program/exit command interpreter"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program incase of non-interactive mode"""
        print()
        return True

    def emptyline(self):
        """if you hit enter key with out entering any command
           on the command line the interpretor repeats the last command
           if you didnt override the 'emptyline' method like this
        """
        pass

    def do_create(self, line):
        """
          create new instance of BaseModel, save it to JSON file
          and print the created instance id.
          if classname missing: print "class name missing"
          if classname doesnt exist: print "class doesn't exist"
          usage: create <class name>
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line in HBNBCommand.name_classes:
            object = HBNBCommand.name_classes.get(line)()
            object.save()
            print(object.id)
        else:
            print("** class name doesn't exist **")

    def do_show(self, line):
        """
          Prints the string representation of an instance
           based on the class name and id

         Usage: show <class name> <id>
        """
        list_arg = line.split()
        if len(list_arg) == 0:
            print("** class name missing **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif not list_arg[0] in HBNBCommand.name_classes:
            print("** class doesn't exist **")
        else:
            dict_of_objs = storage.all()
            key = "{}.{}".format(list_arg[0], list_arg[1])
            if key in dict_of_objs.keys():
                print(dict_of_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
          Delete an instance based on the class name and id and
          save the change into the JSON file
        """
        list_arg = line.split()
        if len(list_arg) == 0:
            print("** class name missing **")  # example: $ destroy
        elif len(list_arg) == 1:
            print("** instance id missing **")  # example: $ destyor User
        elif not list_arg[0] in HBNBCommand.name_classes:
            print("** class doesn't exist **")
        else:
            dict_of_objs = storage.all()
            key = "{}.{}".format(list_arg[0], list_arg[1])
            if key in dict_of_objs.keys():
                storage.delete(list_arg[0], list_arg[1])
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
          Print all string representation of all instances
          based or not on the class name
        """
        if (line == ""):
            list_obj = list(storage.all().values())
            print(list(map(lambda x: str(x), list_obj)))
        elif line in HBNBCommand.name_classes:
            list_obj = list(storage.all().values())
            list_obj = filter(lambda x: type(x) is
                              HBNBCommand.name_classes.get(line), list_obj)
            print(list(map(lambda x: str(x), list_obj)))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
          Update an instance based on the class name and id
          by adding or updating attribute and
          save the change in to JSON file.
          Only one attribute can be updated at the time.
        """
        list_arg = shlex.split(line)
        if len(list_arg) == 0:
            print("** class name missing **")
        elif not list_arg[0] in HBNBCommand.name_classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(list_arg[0], list_arg[1])
              not in storage.all().keys()):
            print("** no instance found **")
        elif len(list_arg) == 2:
            print("** attribute name missing **")
        elif len(list_arg) == 3:
            print("** value missing **")
        else:
            dict_objs = storage.all()
            aux = "{}.{}".format(list_arg[0], list_arg[1])
            if aux in dict_objs.keys():
                attr = getattr(dict_objs[aux], list_arg[2], "")
                setattr(dict_objs[aux], list_arg[2], type(attr)(list_arg[3]))
                dict_objs[aux].save()

    @staticmethod
    def all_class(*args):
        '''call all instaces of obj'''
        dummy = HBNBCommand()
        dummy.do_all(args[0])

    @staticmethod
    def count_class(*args):
        '''count all instaces of obj'''
        list_obj = list(storage.all().values())
        list_obj = filter(lambda x: type(x) is
                          HBNBCommand.name_classes.get(args[0]), list_obj)
        print(len(list(list_obj)))

    @staticmethod
    def show_class(*args):
        ''' show an intances '''
        dummy = HBNBCommand()
        dummy.do_show(" ".join(args))

    @staticmethod
    def destroy_class(*args):
        ''' destroy an intance '''
        dummy = HBNBCommand()
        dummy.do_destroy(" ".join(args))

    @staticmethod
    def update_class(*args):
        ''' update an intance '''
        dummy = HBNBCommand()
        if len(args) == 3 and type(args[2]) is dict:
            for attr, val in args[2].items():
                tmp = list(args[0:2]) + [attr, str(val)]
                dummy.do_update(" ".join(tmp))
        else:
            dummy.do_update(" ".join(args))

    name_dotcommand = {".all()": "HBNBCommand.all_class",
                       ".count()": "HBNBCommand.count_class",
                       ".show()": "HBNBCommand.show_class",
                       ".destroy()": "HBNBCommand.destroy_class",
                       ".update()": "HBNBCommand.update_class"}

    def do_User(self, line):
        '''functions for User:

        '''
        cmd_args = line[line.find("(") + 1:line.find(")")]
        cmd_line = line.replace(cmd_args, "")
        if cmd_line in HBNBCommand.name_dotcommand:
            eval(HBNBCommand.name_dotcommand[cmd_line] + "({})"
                 .format("'User', " + cmd_args))

    def do_State(self, line):
        '''functions for State:

        '''
        cmd_args = line[line.find("(") + 1:line.find(")")]
        cmd_line = line.replace(cmd_args, "")
        if cmd_line in HBNBCommand.name_dotcommand:
            eval(HBNBCommand.name_dotcommand[cmd_line] + "({})"
                 .format("'State', " + cmd_args))

    def do_City(self, line):
        '''functions for City:

        '''
        cmd_args = line[line.find("(") + 1:line.find(")")]
        cmd_line = line.replace(cmd_args, "")
        if cmd_line in HBNBCommand.name_dotcommand:
            eval(HBNBCommand.name_dotcommand[cmd_line] + "({})"
                 .format("'City', " + cmd_args))

    def do_Amenity(self, line):
        '''functions for Amenity:

        '''
        cmd_args = line[line.find("(") + 1:line.find(")")]
        cmd_line = line.replace(cmd_args, "")
        if cmd_line in HBNBCommand.name_dotcommand:
            eval(HBNBCommand.name_dotcommand[cmd_line] + "({})"
                 .format("'Amenity', " + cmd_args))

    def do_Place(self, line):
        '''functions for Place:

        '''
        cmd_args = line[line.find("(") + 1:line.find(")")]
        cmd_line = line.replace(cmd_args, "")
        if cmd_line in HBNBCommand.name_dotcommand:
            eval(HBNBCommand.name_dotcommand[cmd_line] + "({})"
                 .format("'Place', " + cmd_args))

    def do_Review(self, line):
        '''functions for Review:

        '''
        cmd_args = line[line.find("(") + 1:line.find(")")]
        cmd_line = line.replace(cmd_args, "")
        if cmd_line in HBNBCommand.name_dotcommand:
            eval(HBNBCommand.name_dotcommand[cmd_line] + "({})"
                 .format("'Review', " + cmd_args))

    def do_BaseModel(self, line):
        '''functions for BaseModel:

        '''
        cmd_args = line[line.find("(") + 1:line.find(")")]
        cmd_line = line.replace(cmd_args, "")
        if cmd_line in HBNBCommand.name_dotcommand:
            eval(HBNBCommand.name_dotcommand[cmd_line] + "({})"
                 .format("'BaseModel', " + cmd_args))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
