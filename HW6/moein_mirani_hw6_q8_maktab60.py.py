def dec(fun):
    def wrapper(*args):
        value=fun(*args)
        return 2*value
    return wrapper

@dec
def myfunction(a,b):
    return a+b

print(myfunction(5,5))
