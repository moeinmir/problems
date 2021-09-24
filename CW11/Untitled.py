
from pprint import pprint
import requests
params = {'results': 20, "gender": "female","inc": "gender"}
header = {"results": "100", "format": "pretty"}
response = requests.get("https://randomuser.me/api",
                        headers=header, params=params)
a = response.json()
print(a)

# result=[]
# for i in range(10):
#     for key,value in a.items():
#         value
#         result.append({key:value})
# print(result)
