#!/usr/bin/python3

from sys import argv

l = argv[1]

new_string = l.replace(",", "")
new_list = list(new_string)
new_tuple = tuple(new_list)
new_string = str(new_list) + str(new_tuple)
print(new_string)
