import re
def cell_num_filter(cell_num):
  if re.search("912[0-9]{7}",cell_num):
    return "0"+re.search("912[0-9]{7}",cell_num).group()
  else:
    return "invalid phone number"

print(cell_num_filter("+989121111111"))
print(cell_num_filter("+98921111111"))

