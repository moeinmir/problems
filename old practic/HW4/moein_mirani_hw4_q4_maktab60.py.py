import os
import os.path
import linecache
directory=input("enter a directpry")
files=[]
for i in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,i)):
        files.append(i)


for i in files:
    with open(os.path.join(directory,i)) as filler:
        k=0
        while k!="":
            k=filler.readline()
            with open("results.txt","a") as writer:
                        writer.write(k)
    with open("results.txt","a") as writer:
            writer.write("\n")
          
with open("results.txt") as filler:
    l=filler.readlines()
l.sort()
l=[i for i in l if i!="\n"]
with open("results.txt","w") as final:
    for i in l:
        final.write(i)
with open("results.txt") as output:
    line_count=0
    for line in output:
        line_count+=1
        if 5<line_count<11:
            print(line)
        if line_count>=11:
            break
    




#/media/ubonto/L/pyt/hom/HW4
