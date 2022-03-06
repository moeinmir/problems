lst=[-1000, 500, -600, 700, 5000, -90000, -175000]
lst_result=list(map(lambda x : -x, list(filter(lambda x: x<0, lst))))
print(lst_result)
