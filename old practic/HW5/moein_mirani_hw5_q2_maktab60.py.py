from math import pi
class Sphere:
    def __init__(self,r):
        self.r=r
        if self.r <= 0:
            raise Exception ("the entry is invalid")
    def area(self):
        return pi*self.r**2
    def circumference(self):
        return 2*pi*self.r



