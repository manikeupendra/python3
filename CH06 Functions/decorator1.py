def f1(f):
    def f2():
        print("function before call")
        f()
        print("function after  call")
    return f2

@f1
def f3():
    print("Calling f3")


f3()




