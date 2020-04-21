class Bunny:
    def __init__(self,n):
        self._n=n

    def __str__(self):
        return F"str: The number of bunniens is {self._n}"
    def __repr__(self):
        return F"repr: The number of bunniens is {self._n}"

obj=Bunny(45)
print(obj)
print(repr(obj))

print(ascii(obj))
print(chr(12355))
print(ord("ぃ"))
