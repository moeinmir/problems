def dec(fun):
    def wrapper(*args):
        value=fun(*args)
        for arg in args:
            if arg%2==1:
                raise Exception(ValueError ("enter even numbers"))
        return value
    return wrapper

@dec
def myfunction(a,b):
    return a+b

print(myfunction(2,2))
