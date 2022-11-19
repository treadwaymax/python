#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'Hello, World.'
print(repr(s))

class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'repr: the number of bunnies is {self._n}'
    def __str__(self):
        return f'str: the number of bunnies is {self._n}'

x = bunny(47)
s = bunny(47)
print(x)
print(chr(128406)) #Emoji for live long and prosper
print(ord('a'))

x = (1, 2, 3, 4, 5)
y = len(x)
y = list(reversed(x))
y = reversed(x)
for i in y: print(i)
y = sum(x)
y = max(x)
print(f'max: {y}')
y = min(x)
print(x)
print(y)

#any
x = (1, 0, 0, 0, 5)
y = any(x)
print(f'any: {y}')

#all
x = (1, 2, 3, 4, 5)
y = all(x)
print(f'all: {y}')

#zip
x = (1, 2, 3, 4, 5)
y = (6, 7, 8, 9, 10)
z = zip( x, y )
for a, b in z: print(f'{a} - {b}')

#enumerate
x = ('cat', 'dog', 'rabbit', 'velicraptor')
for i, v in enumerate(x): print(f'{i}: {v}')

#object and class functions
x=42
y=type(x)
y=isinstance(x, int)
y=id(x)
print(x)
print(y)