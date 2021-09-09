def my_gen(x,n):
    for i in range(1,n):
        yield i*x

x=my_gen(5,20)
print(next(x))
print(next(x))
print(next(x))
    
