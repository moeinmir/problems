import os
import os.path
directory=input("enter a directory")
number_of_files=0
number_of_folders=0
for i in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,i)):
        number_of_files+=1
    if os.path.isdir(os.path.join(directory,i)):
        number_of_folders+=1
print(f"number of folders: {number_of_folders}")
print(f"number of files: {number_of_files}")



