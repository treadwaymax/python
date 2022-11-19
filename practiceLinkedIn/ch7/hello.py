#!/usr/bin/env python3

def f1(f):
    def f2():
        print('ayyy')
        f()
        print('chee')
    return f2

@f1
def f3():
    print('ish')

f3()
