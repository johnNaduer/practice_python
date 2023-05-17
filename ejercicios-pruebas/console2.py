#!/usr/bin/python3
import cmd
import models
from models.base_model2 import basemodel
""" from models.db_storage import DBStorage """

from models.state2 import state

classes = {'basemodel':basemodel, 'state':state}

class HBNBCcommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ exit program """
        return True

    def do_EOF(self, line):
        """ exit by ctrl + D """
        return True

    def do_create(self, line):
        """ create basemodel for dates"""
        args = line.split(" ")
        print(args[0])
        print(type(args[0]))
        x = 1
        y = 2
        datos = {}
        i = 0
        while i < len(args):
            if x < len(args) and y < len(args):
                datos[args[x]] = args[y]
            else:
                break
            x = x + 2
            y = y + 2
            i = i + 1

        if args[0] in classes:
            instance = classes[args[0]](**datos)
            print(instance.id)

    def do_all(self, line):
        """ print all elements """
        args = line.split(" ")
        instance = models.estorage.all(classes[args[0]])
        print(instance)
        for obj in instance:
            print("{} - {}".format(obj.id, obj.name))

if __name__ == '__main__':
    HBNBCcommand().cmdloop()
