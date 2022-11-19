#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 42

if x > y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x == y:
    print('x == y: x is {} and y is {}'.format(x, y))
else:
    print('do something else')