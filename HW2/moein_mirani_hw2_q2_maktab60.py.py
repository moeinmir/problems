from random import randint

class Game:
    def __init__(self):
        self.board = ["O"]*9
        self.positions1=[]
        self.positions2=[]
        self.winnig_sets=[{(1,1),(1,2),(1,3)},{(2,1),(2,2),(2,3)},{(3,1),(3,2),(3,3)},{(1,1),(2,1),(3,1)},{(1,2),(2,2),(3,2)},{(1,3),(2,3),(3,3)},{(1,1),(2,2),(3,3)},{(1,3),(2,2),(3,1)}]
    def player(self):
        while True:
            a,b=list(map(int,input('enter the row number and column number, seperate them with space and press enter').split()))
            if self.board[(a-1)*3+b-1]=="O":
                self.board[(a-1)*3+b-1]="+"
                self.positions1.append((a,b))
                break
            else:
                print("enter a valid position")

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i*3+j],end=" ")
            print('')
    def robot(self):
        while True:
            a=randint(1,3)
            b=randint(1,3)
            if self.board[(a-1)*3+b-1]=="O":
                self.board[(a-1)*3+b-1]="_"
                self.positions2.append((a,b))
                break
    def play(self):
        self.e=Game()
        if randint(1,2)==1:
            while True:
                self.e.player()
                self.e.show()
                if self.e.win1()==False:
                    break
                else:
                    if self.e.draw()==False:
                        break
                self.e.robot()
                self.e.show()
                if self.e.win2()==False:
                    break
                else:
                    if self.e.draw()==False:
                        break
        else:
            while True:
                self.e.robot()
                self.e.show()
                if self.e.win2()==False:
                    break
                else:
                    if self.e.draw()==False:
                        break
                self.e.player()
                self.e.show()
                if self.e.win1()==False:
                    break
                else:
                    if self.e.draw()==False:
                        break
    def win1(self):
        for i in self.winnig_sets:
            if i <= set(self.positions1):
                print("you won")
                return False
    def draw(self):
                if len(self.positions1)+len(self.positions2)==3**2:
                    print("draw")
                    return False
    def win2(self):
        for i in self.winnig_sets:
            if i <= set(self.positions2):
                print("the computer won")
                return False


##Game().play()



class SmartGame:
    def __init__(self):
        self.board = ["O"]*9
        self.positions1=[]
        self.positions2=[]
        self.winnig_sets=[{(1,1),(1,2),(1,3)},{(2,1),(2,2),(2,3)},{(3,1),(3,2),(3,3)},{(1,1),(2,1),(3,1)},{(1,2),(2,2),(3,2)},{(1,3),(2,3),(3,3)},{(1,1),(2,2),(3,3)},{(1,3),(2,2),(3,1)}]
    def player(self):
        while True:
            a,b=list(map(int,input('enter the row number and column number, seperate them with space and press enter').split()))
            if self.board[(a-1)*3+b-1]=="O":
                self.board[(a-1)*3+b-1]="+"
                self.positions1.append((a,b))
                break
            else:
                print("enter a valid position")

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i*3+j],end=" ")
            print('')
    def robot(self):
            if len(self.positions1)+len(self.positions1)==0:
                    a,b=2,2
                    self.board[(a-1)*3+b-1]="_"
                    self.positions2.append((a,b))             
            elif self.my_last_move()!=None:
                    a,b=self.my_last_move()
                    self.board[(a-1)*3+b-1]="_"
                    self.positions2.append((a,b))
            elif self.last_move()!=None:
                    a,b=self.last_move()
                    self.board[(a-1)*3+b-1]="_"
                    self.positions2.append((a,b))
            elif self.my_last_move1()!=None:
                    a,b=self.my_last_move1()
                    self.board[(a-1)*3+b-1]="_"
                    self.positions2.append((a,b))
            elif self.last_move1()!=None:
                    a,b=self.last_move1()
                    self.board[(a-1)*3+b-1]="_"
                    self.positions2.append((a,b))    
            else:
                while True:
                    a=randint(1,3)
                    b=randint(1,3)
                    if self.board[(a-1)*3+b-1]=="O":
                        self.board[(a-1)*3+b-1]="_"
                        self.positions2.append((a,b))
                        break
    def play(self):
        self.e=SmartGame()
        if randint(1,2)==1:
            while True:
                self.e.player()
                self.e.show()
                if self.e.win1()==False:
                    break
                else:
                    if self.e.draw()==False:
                        break
                self.e.robot()
                self.e.show()
                if self.e.win2()==False:
                    break
                else:
                    if self.e.draw()==False:
                        break
        else:
            while True:
                self.e.robot()
                self.e.show()
                if self.e.win2()==False:
                    break
                else:
                    if self.e.draw()==False:
                        break
                self.e.player()
                self.e.show()
                if self.e.win1()==False:
                    break
                else:
                    if self.e.draw()==False:
                        break
    def win1(self):
        for i in self.winnig_sets:
            if i <= set(self.positions1):
                print("you won")
                return False
    def draw(self):
                if len(self.positions1)+len(self.positions2)==3**2:
                    print("draw")
                    return False
    def win2(self):
        for i in self.winnig_sets:
            if i <= set(self.positions2):
                print("the computer won")
                return False

    def last_move(self):
        for i in range(len(self.positions1)):
            for j in range(i+1,(len(self.positions1))):
                self.c=set({})
                self.c.add(self.positions1[i])
                self.c.add(self.positions1[j])
                for k in range(len(self.winnig_sets)):
                    if self.c<=self.winnig_sets[k]:
                        if self.board[(list((self.winnig_sets[k]-self.c))[0][0]-1)*3+list((self.winnig_sets[k]-self.c))[0][1]-1]=="O":
                            return list((self.winnig_sets[k]-self.c))[0]

    def my_last_move(self):
        for i in range(len(self.positions2)):
            for j in range(i+1,(len(self.positions2))):
                self.d=set({})
                self.d.add(self.positions2[i])
                self.d.add(self.positions2[j])
                for k in range(len(self.winnig_sets)):
                    if self.d<=self.winnig_sets[k]:
                        if self.board[(list((self.winnig_sets[k]-self.d))[0][0]-1)*3+list((self.winnig_sets[k]-self.d))[0][1]-1]=="O":
                            return list((self.winnig_sets[k]-self.d))[0]


    def last_move1(self):
        for i in range(len(self.positions1)):
                self.f=set({})
                self.f.add(self.positions1[i])
                for k in range(len(self.winnig_sets)):
                    if self.f<=self.winnig_sets[k]:
                        if self.board[(list((self.winnig_sets[k]-self.f))[0][0]-1)*3+list((self.winnig_sets[k]-self.f))[0][1]-1]=="O":
                            return list((self.winnig_sets[k]-self.f))[0]

    def my_last_move1(self):
        for i in range(len(self.positions2)):
                self.g=set({})
                self.g.add(self.positions2[i])
                for k in range(len(self.winnig_sets)):
                    if self.g<=self.winnig_sets[k]:
                        if self.board[(list((self.winnig_sets[k]-self.g))[0][0]-1)*3+list((self.winnig_sets[k]-self.g))[0][1]-1]=="O":
                            return list((self.winnig_sets[k]-self.g))[0]




                    
SmartGame().play()




    











