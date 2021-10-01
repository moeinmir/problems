lst1=[1000,500,600,700,5000,90000,175000]

def add(x):
    if x<8000:
        return x+8000
    else:
        return x

lst_added=lambda lst: list(map(add,lst))

print(lst_added(lst1))

#or we could get the list from user
lst2=list(map(int,(input("enter numbers with space between").split())))
print(lst_added(lst2))
