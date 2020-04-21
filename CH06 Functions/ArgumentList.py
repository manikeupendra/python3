def name():
    n=("ram","sma","bam")
    printName(*n)

def printName(*args):
    if len(args):
        for i in args:
            print(i)
def main():
    name()

if __name__ == "__main__":
    main()
