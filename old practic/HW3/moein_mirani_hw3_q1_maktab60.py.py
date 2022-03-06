from random import random
class Shooter:
    distance=500
    results=[]
    errors_sum=0
    ave_error=0
    number_of_shooters=0
    def __init__(self,player_number,player_name,height,weight):
        self.player_number=player_number
        self.player_name=player_name
        self.height=height
        self.weight=weight
        self.point_index=random()*1.5+0.5
        self.error=(self.height-self.weight)*self.point_index
        Shooter.number_of_shooters+=1
        Shooter.errors_sum=Shooter.errors_sum+self.error
        Shooter.ave_error=Shooter.errors_sum/Shooter.number_of_shooters
        Shooter.results.append(self)
        Shooter.sort_the_list()
    @classmethod
    def sort_the_list(cls):
         for i in range(len(cls.results)-1):
             for j in range(len(cls.results)-1):
                 if cls.results[j].error>cls.results[j+1].error:
                     a=cls.results[j]
                     b=cls.results[j+1]
                     cls.results[j]=b
                     cls.results[j+1]=a
    @classmethod
    def show_results(cls):
        print("average error:",cls.ave_error)
        for i in cls.results:
            print(i.player_number,"\t",i.player_name,"\t",i.height,"\t",i.weight,"\t","{:.02f}".format(i.error))


names=["name1","name2","name3","name4","name5"]
heights=[180,160,175,160,195]
weights=[60,75,90,85,95]
#we dont even have to make another list and save the instances in it
for i in range(len(names)):
    Shooter(i+1,names[i],heights[i],weights[i])

Shooter.show_results()    

                   
                
        
        
            


