#!/usr/bin/python3
from sys import argv

x = int(argv[1])
x2 = 1
while x > 0:
    x2 = x2*x
    x = x - 1
print(x2)
