basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

rs='orange' in basket 
if rs:
    print("Orange in basket")
else:
    print("Orange is not in basket")


a = set('abracadabra')
b = set('alacazam')
# unique letters in a
print(a)
# unique letters in b
print(b)
# letters in a but not in b
print(a - b)
# letters in a or b or both

print(a | b)
# letters in both a and b
print(a & b )

# letters in a or b but not both
print(a ^ b  )