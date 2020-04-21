x=[1,2,3,4,5]
print("--------------List-------------- ")
print("List before update")
for i in x:
    print("i value is {} .".format(i))

print("-------------------------------- ")
x[0]=100
print("--------------List-------------- ")
print("List after update")
for i in x:
    print("i value is {} .".format(i))

print("-------------------------------- ")

y=(1,2,3,4,5)
print("--------------Touple-------------- ")
for i in y:
    print("i value is {} .".format(i))
print("-------------------------------- ")

''' List values can reassigin
    Touple if final we cannot modify 
'''
