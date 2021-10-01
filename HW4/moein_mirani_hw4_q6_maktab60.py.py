import os
import os.path
import shutil
directory1=input("enter a directory")
directory2=input("enter the second directory")
def containig_a(file):
    if "a" in file:
        return True
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

files=[]
for i in os.listdir(directory1):
    if os.path.isfile(os.path.join(directory1,i)) and containig_a(i) and is_ascii(open(os.path.join(directory1,i)).read()):
                      shutil.copy2(os.path.join(directory1,i),directory2)
                  






