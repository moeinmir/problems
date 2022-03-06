

class Student:
    def __init__(self,weight,height,age):
        self.weight=weight
        self.height=height
        self.age=age

class ClassRoom:
    def __init__(self,seats,ages,weights,heights):
        self.weight_ave=0
        self.height_ave=0
        self.age_ave=0
        self.seats=seats
        self.heights=heights
        self.weights=weights
        self.student=Student
        self.book=[]
        for i in range(seats):
            c=Student(weights[i],heights[i],ages[i])
            self.book.append(c)
            self.weight_ave=self.weight_ave+c.weight
            self.height_ave=self.height_ave+c.height
            self.age_ave=self.age_ave+c.age
        self.weight_ave=self.weight_ave/seats
        self.height_ave=self.height_ave/seats
        self.age_ave=self.age_ave/seats
    def __str__(self):
        return f"{self.age_ave}\n{self.weight_ave}\n{self.height_ave}"

def cmp(classroom1,classroom2):
        print (classroom1.seats)
        for i in range(classroom1.seats):
            print(classroom1.book[i].age,end=" ")
        print()
        for i in range(classroom1.seats):
            print(classroom1.book[i].height,end=" ")
        print()
        for i in range(classroom1.seats):
            print(classroom1.book[i].weight,end=" ")
        print()
        print (classroom2.seats)
        for i in range(classroom2.seats):
            print(classroom2.book[i].age,end=" ")
        print()
        for i in range(classroom2.seats):
            print(classroom2.book[i].height,end=" ")
        print()
        for i in range(classroom2.seats):
            print(classroom2.book[i].weight,end=" ")
        print()
        print("{:0.02f}".format(classroom1.age_ave))
        print("{:0.02f}".format(classroom1.height_ave))
        print("{:0.02f}".format(classroom1.weight_ave))
        print("{:0.02f}".format(classroom2.age_ave))
        print("{:0.02f}".format(classroom2.height_ave))
        print("{:0.02f}".format(classroom2.weight_ave))
        if classroom1.weight_ave>classroom2.weight_ave and classroom1.height_ave>classroom2.height_ave:
            print("A")
        if classroom1.weight_ave<classroom2.weight_ave and classroom1.height_ave<classroom2.height_ave:
            print("B")
        if classroom1.weight_ave==classroom2.weight_ave and classroom1.height_ave==classroom2.height_ave:
            print("the same")
        else:
            print("vage")

An=int(input("enter the number of student in class A"))
Aa=list(map(int,input("enter the ages of students in class A, seperate them with spaces").split()))
Ah=list(map(int,input("enter the heights of student in class A, seperate them with spaces").split()))
Aw=list(map(int,input("enter the weights of student in class A, seperate them with spaces").split()))


Bn=int(input("enter the number of students in class B"))
Ba=list(map(int,input("enter the ages of students in class B, seperate them with spaces").split()))
Bh=list(map(int,input("enter the heights of students in class B, seperate them with spaces").split()))
Bw=list(map(int,input("enter the weights of students in class B, seperate them with space").split()))


classA=ClassRoom(An,Aa,Aw,Ah)
classB=ClassRoom(Bn,Ba,Bw,Bh)
cmp(classA,classB)



