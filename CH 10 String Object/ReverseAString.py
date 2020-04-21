class ReverseMyString(str):
    def __str__(self):
        return self[::-1]

a=ReverseMyString("Hello. Python")
print(a)