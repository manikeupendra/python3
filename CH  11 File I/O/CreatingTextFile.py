# file = open("test.txt", "x") 
# file.write("Your text goes here") 
# file.close() 


file = open("/home/upendra/Documents/python3 Essential/python3/test.txt", "r") 
for i in file:
    print(i.rstrip())
file.close() 