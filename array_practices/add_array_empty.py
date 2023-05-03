#!/usr/bin/python3

numero = [0, 1, 2, 4, 7, 8, 9, 11]

numero4 = numero.copy()
numero4.reverse()
i = 0
numero3 = []

while i < len(numero):
    numero3 = numero3 + [numero[i]]
    i = i + 1

print(numero3)
