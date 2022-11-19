#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        #outfile.writelines(line) #won't translate between OS if different endlines exist
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()
