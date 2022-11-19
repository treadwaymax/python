#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class MyString(str):
    def __str__(self):
        return self[::-1]

s = MyString('Hello, World.')
print(s)

print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.title())
print('Hello, World.'.casefold()) #break down even unicode to lowercase

s1 = 'Hiya'
s2 = 'bitch'
s3 = 'this string' ' that string'
print(s1 +' '+ s2)
print(s3)

x = 42
y = 73
print('the number is {0:<5} {1:+05}'.format(x, y))

a = 42
print('the number is {:,}'.format(a).replace(',', '.'))
print('the number is {:b}'.format(a))
print(f'the number is {a:.3f}')
