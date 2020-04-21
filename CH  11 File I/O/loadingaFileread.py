def main():
    f = open("/home/upendra/Documents/python3 Essential/python3/CH  11 File I/O/lines.txt",'r')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()