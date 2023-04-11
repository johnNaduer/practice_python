#!/usr/bin/python3

from sys import argv

def dict_quare(n=None):
    d = {}
    for i in range(1, int(n) + 1):
        d[i] = i*i
    print(d)

dict_quare(argv[1])
