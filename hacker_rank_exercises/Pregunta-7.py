#!/usr/bin/python3
"""
Nivel 2

Pregunta: escriba un programa que tome 2 dígitos, X, Y como entrada y genere una matriz bidimensional. 
El valor del elemento en la i-ésima fila y la j-ésima columna de la matriz debe ser i*j.
Nota: i=0,1.., X-1; j=0,1,¡Y-1. 
Ejemplo Supongamos que se dan las siguientes entradas al programa: 3,5 Entonces, 
la salida del programa debería ser: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [ 0, 2, 4, 6, 8]]
Sugerencias: Nota: En caso de que se proporcionen datos de entrada a la pregunta, 
se debe suponer que se trata de una entrada de consola separada por comas.
"""

"""
x = '3,5'
y = x.split(',')
n = int(y[0])
m = int(y[1])
dato1 = []
for (i in range(n))
    dato2 = []
    dato2.append('i')*i
"""

x = '4,6'
y = x.split(',')
n = int(y[0])
m = int(y[1])
dato1 = []
dato2 = []
for i in range(n):
    dato2 = []
    for j in range(m):
        dato2 = dato2 + [j*i]
    dato1.append(dato2)
