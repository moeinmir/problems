f=open("abc.txt")
def counter(s):
    ans={}
    for i in range(len(s)):
        if i!=s.index(s[i]):
            continue
        else:
            ans[s[i]]=s.count(s[i])
    return ans
            
print(counter(f.read()))
