#!/usr/bin/python3

from sys import argv

args_list = argv
# Supongamos que el usuario ha pasado algunos argumentos como entrada
# Ejemplo: python mi_programa.py arg1 arg2 arg3
# En este caso, args_list será ['mi_programa.py', 'arg1', 'arg2', 'arg3']

# Queremos trabajar solo con los argumentos después del primer elemento
# Por lo tanto, usamos el slicing de lista para crear una nueva lista
# que contenga solo los argumentos después del primer elemento
# En este caso, la nueva lista será ['arg1', 'arg2', 'arg3']
new_args_list = args_list[1:]

# Podemos utilizar la nueva lista para realizar alguna tarea
# Por ejemplo, podemos imprimir todos los argumentos uno por uno
for arg in new_args_list:
    print(arg)
