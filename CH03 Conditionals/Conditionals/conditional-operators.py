'''
Comparison Operators 
==      a==b    Equal
!=      a!=b    Not Equal
<       a<b     Less Then
>       a>b     Grater Then
<=      a<=b    Less Then or Equal
>=      a>=b    Grater Then or Equal
'''
print("---------------------------------------------------")
print("--------------Comparison Operators-----------------")
print("---------------------------------------------------\n")

print("-----------------------Equal-----------------------")
a=10
b=10
if a==b:
    print("  a={} and b={} a==b is true ".format(a,b))

print("---------------------------------------------------")
print("-------------------Not Equal-----------------------")
a=10
b=100
if a!=b:
    print("  a={} and b={} a!=b is true ".format(a,b))

print("---------------------------------------------------")

print("-------------------Less Then-----------------------")
a=10
b=100
if a<b:
    print("  a={} and b={} a<b is true ".format(a,b))

print("---------------------------------------------------")


print("-----------------Grater Then-----------------------")
a=1000
b=100
if a>b:
    print("  a={} and b={} a>b is true ".format(a,b))

print("--------------------------------------------------------")
print("------------------Less Then or Equal--------------------")
a=100
b=100
if a<=b:
    print("  a={} and b={} a<=b is true ".format(a,b))

print("----------------------------------------------------------")

print("-----------------Grater Then  or Equal--------------------")
a=1000
b=1000
if a>=b:
    print("  a={} and b={} a>=b is true ".format(a,b))

print("----------------------------------------------------------")
'''
Logical Operators


'''
print("##########################################################")
print("==================Logical Operators=======================")
print("##########################################################")

print("######################## and #############################")   

if True and True:
    print(" both the conditions true only and will execute ")
print("######################## or  #############################")   

if True or False:
    print(" any conditions true only and will execute ")
print("######################## not #############################")   

if not False:
    print(" both are not conditions true only and will execute ")
print("##########################################################")




