#!/usr/bin/python3
l = []
n = 2000
while n <= 3200:
    if n % 7 == 0 and n % 35 != 0:
        l.append(str(n))
    n = n + 1

nuevo = ', '.join(l)
print(nuevo)
