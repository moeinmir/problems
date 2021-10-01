def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print("the index is invalid")
print_list_element([1,2,3],3)