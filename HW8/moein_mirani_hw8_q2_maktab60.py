from datetime import date
def format_time(year,mounth,day):
  date_entry=date(year,mounth,day)
  a=date_entry.strftime("%a")
  b=date_entry.strftime("%b")
  c=date_entry.year
  return str(a)+"_"+str(b)+"_"+str(c)


print(format_time(2020,11,11))

