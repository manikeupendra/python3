#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('/home/upendra/Documents/python3 Essential/python3/CH  11 File I/O/berlin.jpg', 'rb')
    outfile = open('/home/upendra/Documents/python3 Essential/python3/CH  11 File I/O/berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
