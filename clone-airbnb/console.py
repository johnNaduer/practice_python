#!/usr/bin/python3

import cmd
from models.elemento_4 import BaseModel
from models.elemento_4 import estorage
from models.state import State

class HBNBCcommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel}

    """
    __clases = {
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
    }
    """
    def do_quit(self, line):
        """ exit program """
        return True

    def do_EOF(self, line):
        """ exit by ctrl + D """
        print()
        return True

    def do_create(self, args):
        """ create ID """
        try:
            if not args:
                raise SyntaxError()
            my_list = args.split(" ")
            obj = eval("{}()".format(my_list[0]))

            for i in range(1, len(my_list)):
                item = my_list[i].split('=')
                key = item[0]
                val = item[1].replace('_', ' ')
                val = val.replace("\"", "")
                try:
                    val = eval(val)
                except:
                    pass

                setattr(obj, key, val)
            obj.save()
            print("{}".format(obj.id))

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, line):
        """ Print all objects """
        objects = estorage.all()
        for obj_key in objects:
            print(objects[obj_key])

if __name__ == '__main__':
    HBNBCcommand().cmdloop()
