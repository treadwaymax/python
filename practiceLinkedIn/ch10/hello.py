#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys

def main():
    try:
        x = 5/'ass'
    except ValueError:
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('Don\'t divide by 0')
    except:
        print(f'unknown error: {sys.exc_info()[1]}')
    else:
        print('good job')
        print(x)
    print('Hello, World.')

if __name__ == '__main__': main()
