import os
#suppose we have the files in the directory belo
dir=r"F:\pyt\hom\HW6\New folder"
files_list=os.listdir(dir)

def gen(files):
    for i in range(len(files)):
            yield os.path.join(dir,files[i-i//(len(files))*len(files)])
        
x=gen(files_list)

def read_lines(files):
        x=files
        for i in x:
            with open(os.path.join(r"F:\pyt\hom\HW6\New folder",i)) as reader:
                    for j in reader:
                        inp=input("enter")
                        if inp!="n":
                            print(j)
                        if inp=="n":
                            #first i thought that i shoud put the next(x) command here,but if i do that it will go two page futher
                            #it works fine with out "next"
                            read_lines(files)
        if input("you reached the end if you want to continue press c and enter")=="c":
                read_lines(x)


read_lines(files_list)
