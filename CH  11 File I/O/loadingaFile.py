'''

open(filedir)

open(filedir,'r')

open(filedir,'r+')
text mode 
open(filedir,'r+t')
binary mode
open(filedir,'r+b')
'''

def main():
    f = open("/home/upendra/Documents/python3 Essential/python3/CH  11 File I/O/lines.txt")
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()