from math import *


class Shape:

  def __init__(self,length,heigth,angle):
    self.length=length
    self.heigth=heigth
    self.angle=angle
    self.width=self.heigth

  def area(self):
    return self.length*self.heigth

  def circumference(self):
    return (self.length+self.width)*2

  def draw(self):
    for i in range(int(self.heigth)):
      for j in range(int(self.length)):
        print("*",end="")
      print()


class Square(Shape):

  def __init__(self,length,heigth=0,angle=pi/2):
    super().__init__(length,heigth,angle)
    self.width=length
    self.length=length
    self.heigth=length


class Rectangle(Shape):

  def __init__(self,length,heigth,angle=pi/2):
    super().__init__(length,heigth,angle)
    self.width=heigth
    self.length=length
    self.heigth=heigth


class Parallelogram(Shape):

  def __init__(self,length,heigth,angle):
    super().__init__(length,heigth,angle)
    self.length=length
    self.heigth=heigth
    self.angle=angle
    self.width=self.heigth/sin(self.angle)

  def draw(self):
    for i in range(int(self.heigth)):
      s=int((self.heigth-i)*cos(self.angle)/sin(self.angle))*" "+self.length*"*"
      print(s)


class Rhombus(Shape):

  def __init__(self,length,heigth=0,angle=pi/2):
    super().__init__(length,heigth,angle)
    self.length=length
    self.heigth= self.length*0.5*2**(0.5)
    self.angle=angle
    self.width=self.length

  def draw(self):
    for i in range(int(self.heigth)):
      s=int((self.heigth-i)*0.5*2**(0.5))*" "+self.length*"*"
      print(s)


class Diamond(Shape):

  def __init__(self,length,heigth=0,angle=pi/2):
    super().__init__(length,heigth,angle)
    self.width=length
    self.length=length
    self.heigth=length
    self.diameter=self.length*2**0.5

  def draw(self):
    for i in range(int(self.diameter/2)):
      print(int(self.diameter/2-i)*" "+int(2*i)*"*"+int(self.diameter/2-i)*" ")
    for i in range(int(self.diameter/2)):
      print(i*" "+2*int(self.diameter/2-i)*"*"+i*" ")

  
a=Square(4)
a.draw()
b=Diamond(10)
b.draw()
print(b.area())

