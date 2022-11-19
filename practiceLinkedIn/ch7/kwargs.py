#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x=dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr'
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()