import re
def thre_typ_exist(s):
  if re.search("\$",s) and re.search("A",s) and re.search('[0-9]',s):
    return True
  else:
    return False

print(thre_typ_exist("$Ahji.1"))
print(thre_typ_exist("Ahji.1"))
  


