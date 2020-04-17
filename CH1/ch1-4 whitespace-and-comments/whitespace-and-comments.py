import platform

def main():
    message()
def message():
    print("Python version is : {} ".format(platform.python_version()))
    print("Line 1 from message")
print("this print method called in out of the method")
#if we execute above code output like "this print method called in out of the method"

if __name__ == "__main__":
    main()
