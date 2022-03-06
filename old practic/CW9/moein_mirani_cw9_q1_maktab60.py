from datetime import time, date, datetime, timedelta

start_time = time(14,00,00)
start_date = date(2018,2,18)
stdt= datetime.combine(start_date,start_time)
period= timedelta(hours=8)
l = []
for i in range(10):
    l.append(stdt+period*i)


y = list(map(int, (input("enter date and time").split())))
now_time = time(y[2], y[4], y[5])
now_dade = date(y[0], y[1], y[2])
nwdt = datetime.combine(now_dade, now_time)


remain_days = 0
for i in l:
    if nwdt < i:
        remain_days+=1
print(remain_days)


for i in l:
    if nwdt < i:
        print(i)
        break
#example entry could be 2018 2 20 11 11 11
