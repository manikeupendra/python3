
def isPrime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    else:
        return True



for i in range(100):
    result=isPrime(i)
    if result ==True:
        print("{} is Prime numbe ".format(i))
    else:
        print("{} is not a prime number".format(i))