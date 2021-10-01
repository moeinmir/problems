


def is_ord_list(small_lst,big_lst):
    a=big_lst.count(small_lst[0])
    for i in range(big_lst.count(small_lst[0])):
        if big_lst[big_lst.index(small_lst[0]):big_lst.index(small_lst[0])+len(small_lst)+1]==small_lst:
            return True
            break
        elif i==a-1:
            return False
            break
        else:
            big_lst.remove(small_lst[0])
            
b=is_ord_list([2,3,4],[45,2,4,7,2,3,4])
print(b)


