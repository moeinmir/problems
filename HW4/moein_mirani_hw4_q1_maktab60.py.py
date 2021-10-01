class Work:
    
    def __init__(self,title,*args):
        self.title=title
        self.owners=args
        if self.is_valid()==False:
            print("the creator is not valid")


    def is_valid(self):# it would be more reseonable to difine this function in each child class, but as the question asked i put it here
        flag=True
        if isinstance(self,Poetry)==True:
            for i in self.owners:
                if isinstance(i,Poet)==False:
                    flag=False
            return flag 
        if isinstance(self,Book)==True:
            for i in self.owners:
                if isinstance(i,Writer)==False:
                    flag=False
            return flag
        if isinstance(self,Article)==True:
            for i in self.owners:
                if isinstance(i,Researcher)==False:
                    flag=False
            return flag 


class Article(Work):
    
    def __init__(self,title,*args,magezine="unknown",publish_year="unknown"):
        super().__init__(title,*args)
        self.magezine=magezine
        self.publish_year=publish_year

    def number_of_owners(self):
        return len(self.owners)

        
class Poetry(Work):
    def __init__(self,title,*args,poetic="unknown"):
        super().__init__(title,*args)
        self.poetic=poetic
        if len(self.owners)>1:
            print("a poetry have only one creator")


class Book(Work):
    number_of_books=0
    
    def __init__(self,title,ISBN,*args,publisher="unknown"):
        super().__init__(title,*args)
        self.ISBN=ISBN
        self.publisher=publisher
        Book.number_of_books+=1
        
    def number_of_owners(self):
        return len(self.owners)
    
    def __del__(self):
        Book.number_of_books-=1
        del self


class Person:
    
    def __init__(self,name,Email="unknown",gender="unknown"):
        self.name=name
        self.Email=Email
        self.gender=gender


class Researcher(Person):
    
    def __init__(self,name,field,Email="unknown",gender="unknown",university="unknown"):
        super().__init__(name,Email,gender)
        self.field=field
        self.university=university


class Poet(Person):
    
    def __init__(self,name,Email="unknown",gender="unknown",style="unknown"):
        super().__init__(name,Email,gender)
        self.style=style


class Writer(Person):
    
    def __inint__(self,name,writing_code,Email="unknown",gender="unknown",genre="unknown"):
        super().__init__(self,name,Email,gender)
        self.genre=genre


a=Book(1,1)
b=Book(1,1)
print(Book.number_of_books)
del a
print(Book.number_of_books)
c=Poet("shamloo")
f=Book("a","b",c)
print(f.is_valid())
g=Poetry("a",c)
print(g.is_valid())













