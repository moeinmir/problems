from operator import itemgetter
lst=[(19542209,"New York"),(4887871,"Alabama")]
revers_fun=lambda x: (int(str(x[0])[::-1]),x[1][::-1])
lst2=sorted(list(map(revers_fun,lst)),key=itemgetter(1))
#if we want to sort based on last charector after reversing we could do what comes next
lst3=list(map(revers_fun,sorted(lst,key=itemgetter(1))))
print(lst2)
print(lst3)
