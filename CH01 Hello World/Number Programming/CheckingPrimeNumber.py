
def isPrime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    else:
        return True


n=5
result=isPrime(n)
if result ==True:
    print("{} is Prime numbe ".format(n))
else:
    print("{} is not a prime number".format(n))