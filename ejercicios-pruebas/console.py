#!/usr/bin/python3

import cmd
from models.creando_json3 import basemodel, estorage

class HBNBCcommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ exit program """
        return True

    def do_EOF(self, line):
        """ exit by ctrl + D """
        return True

    def do_create(self, line):
        args = line.split(" ")
        instance = basemodel()
        print(instance.id)
        
        
if __name__ == '__main__':
    HBNBCcommand().cmdloop()
