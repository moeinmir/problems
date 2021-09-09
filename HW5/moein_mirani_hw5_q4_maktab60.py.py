def add_to_list(thedict,listname,element):
    try:
        if element in thedict[listname]:
            print(f"{listname} already has {element}")
        else:
            print(f"{element} added to {listname}")
            thedict[listname].append(element)
    except:
        print("the list is invalid")
    finally:
        print("the job is done")

l={"a":[1,2]}
add_to_list(l,"a",5)



                   
                
        
        
            


