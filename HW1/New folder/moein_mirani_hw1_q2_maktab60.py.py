

from random import randint

ave=0
for i in range(10):
    s=''
    c=0
    while True:
        a=randint(1,2)
        c=c+1
        if a==1:
            s+='H'
        if a==2:
            s+='T'
        if 'HHH' in s or 'TTT' in s:
            print('{} {} flips were requierd'.format(s,c))
            ave=ave+c
            break

print('on average {} flipes were requierd'.format(ave/10))
        
        
