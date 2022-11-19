#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

a = Decimal('.10')
b = Decimal('.40')
c = a+a+a+a-b
d = f'a+a+a+a-b'
print ('c is {}'.format(c))
print(type(c))


x = 7
print('x is {}'.format(x))
print(type(x))
