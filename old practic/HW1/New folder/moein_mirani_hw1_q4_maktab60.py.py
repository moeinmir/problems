product_list = [
       {
           "type": "1",
           "name": "shirt",
           "price": 30,
           "unit": "Dollar",
           "commission_groups": ["A", "B"]
       },
       {
           "type": "2",
           "name": "pants",
           "price": 50,
           "unit": "Dollar",
           "commission_groups": ["A", "C"]
       },
       {
           "type": "3",
           "name": "shoes",
           "price": 80,
           "unit": "Dollar",
           "commission_groups": ["B"]
       },
       {
           "type": "4",
           "name": "hat",
           "price": 20,
           "unit": "Dollar",
           "commission_groups": []
       }
]

markup_list = [
    {
        "product_type": "1",
        "lower_cost": 10,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "2",
        "lower_cost": 15,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "3",
        "lower_cost": 10,
        "upper_cost": 15,
        "unit": "percent",
        "lower_count": 5
    },
    {
        "product_type": "4",
        "lower_cost": 10,
        "upper_cost": 30,
        "unit": "percent",
        "lower_count": 20
    },
]

commission_list = [
    {
        "group_name": "A",
        "cost": 5,
        "unit": "percent",
        "users": [1001, 1002, 1003, 1005]
    },
    {
        "group_name": "B",
        "cost": 3,
        "unit": "Dollar",
        "users": [1001, 1003, 1006]
    },
    {
        "group_name": "C",
        "cost": 7,
        "unit": "percent",
        "users": [1001, 1002, 1004]
    }
]


user_list = [
    {
        "userid": 1001,
        "first_name": "Mohsen",
        "last_name": "Bayat",
    },
    {
        "userid": 1002,
        "first_name": "Sobhan",
        "last_name": "Taghadosi",
    },
    {
        "userid": 1003,
        "first_name": "Javad",
        "last_name": "Jafari",
    },
    {
        "userid": 1004,
        "first_name": "Masoud",
        "last_name": "Hosseini",
    },
    {
        "userid": 1005,
        "first_name": "Hassan",
        "last_name": "Zand",
    },
    {
        "userid": 1006,
        "first_name": "Ali",
        "last_name": "Ebadi",
    }
]
#part1 for solving this part i asume that we know that the position of objects in the list is in order and for exampel we can access to type 2 by calling the second member of the list otherwise we should read the whole list to access the information for type "2"
def markup(t,n):
    if n==1:
        return markup_list[t-1]["upper_cost"]
    if 1<n<markup_list[t-1]["lower_count"]:
        return (markup_list[t-1]["upper_cost"]*(markup_list[t-1]["lower_count"]-n)/markup_list[t-1]["lower_count"])+ markup_list[t-1]["lower_cost"]*n/markup_list[t-1]["lower_count"]
    if n>1:
        return markup_list[t-1]["lower_count"]
    
def markupprice(t,n):
    return markup(t,n)*product_list[t-1]["price"]/100
def price(t,n):
    return markup(t,n)*product_list[t-1]["price"]/100+product_list[t-1]["price"]

def Calculate_product_price(product_type, count, userid=0):
    total_price=price(product_type,count)*count
    answer={}
    if userid==0:
        answer["product_name"]=product_list[product_type-1]["name"]
        answer["total_price"]=total_price
        answer["discount"]=0
    else: 
        total_with_commission=total_price
        commission=0
        for i in range(len(commission_list)):
            if userid in commission_list[i]["users"] and commission_list[i]["group_name"] in product_list[product_type-1]["commission_groups"]:
                if commission_list[i]["unit"]=="percent":
                    commission=commission+total_price*commission_list[i]["cost"]/100
                if commission_list[i]["unit"]=="Dollar":
                    commission=commission+commission_list[i]["cost"]
        total_with_commission=total_with_commission-commission
        for i in range(len(user_list)):
            if user_list[i]["userid"]==userid:
                fname=user_list[i]["first_name"]
                lname=user_list[i]["last_name"]
        answer["product_name"]=product_list[product_type-1]["name"]
        answer["total_price"]=total_price
        answer["discount"]=commission
        answer["total_with_commission"]=total_with_commission
        answer["first_name"]=user_list[1001-userid]["first_name"]
        answer["last_name"]=user_list[1001-userid]["last_name"]
    return answer
        
print(Calculate_product_price(1,14,1001))
     
    
