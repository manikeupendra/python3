def main():
    try:
        n=int("foo")
    except ValueError:
        print("Please enter the number not string")

    else:
        print(n)

if __name__ == "__main__":
    main()
   