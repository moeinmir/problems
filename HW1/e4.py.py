s=input('enter a string')
lower_case=0
upper_case=0
for i in s:
    if i.isupper():
        upper_case+=1
    if i.islower():
        lower_case+=1
ans={}
ans["lower_case"]=lower_case
ans["upper_case"]=upper_case
print(ans)
        
