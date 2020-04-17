''' Write a Program to print the String if number divisable by 3 and  5 FizzBuzz if number divisible by 3 Fizz, if number divisible by 5 Buzz
'''

num=15
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")