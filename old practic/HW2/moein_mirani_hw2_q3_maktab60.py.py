class Rectangle():
    def __init__(self,height,width):
        self.height=height
        self.width=width
        self.circumfreence=2*(self.height+self.width)
        self.area=self.height*self.width
    def __str__(self):
        return f"h={self.height} w={self.width} A={self.area} C={self.circumfreence}"
    
a=Rectangle(3,5)
print(a)
print(a.circumfreence)
print(a.area)
