import numpy as np
list_1=[100,200,300,400,500]
list_2=[1,10,100,1000,10000]
answer=list(np.array(list_1)+np.array(list_2))
print(answer)

#another way

answer_other_way=list(map(lambda x,y:x+y,list_1,list_2))
print(answer_other_way)
