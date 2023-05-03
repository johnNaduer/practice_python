#!/usr/bin/python3

import cmd
from models.file_storage import basemodel, estorage
from models.user import user
from models.amenity import amenity
from models.city import city
from models.place import place
from models.state import state
from models.review import review

classes = {'basemodel':basemodel, 'user':user, 'amenity':amenity, 
           'city':city, 'place':place, 'state':state, 'review':review}

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
        """ print all elements"""
        instance = estorage.all()
        print(instance)

if __name__ == '__main__':
    HBNBCcommand().cmdloop()
