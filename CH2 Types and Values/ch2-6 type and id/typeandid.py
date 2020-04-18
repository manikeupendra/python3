x=(1,"name",["hello",3],"t")
y=(1,"name",["hello",3],"t")

# above x and y are holding same values but object reference is diffrent

print(x)
print(y)

print("Address of the x is {}.".format(id(x)))
print("Address of the y is {}.".format(id(y)))

# print 0 index value id
print("Address of the x[0] is {}.".format(id(x[0])))
print("Address of the y[0] is {}.".format(id(y[0])))

#validating x and y

if x is y:
    print("Yes")
else:
    print("No")

