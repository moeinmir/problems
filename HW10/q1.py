import re
from datetime import date, time, datetime
import redis
#redis_client = redis.Redis()
redis_client = redis.Redis(charset="utf-8", decode_responses=True)


class Event:

    # event time string should be like 'Jun 1 2005  1:33PM'

    def __init__(self, event_name, event_time, event_place, event_whole_capacity, event_price):
        self.event_name = event_name
        self.event_time = event_time
        self.event_place = event_place
        self.event_whole_capacity = event_whole_capacity
        self.event_price = event_price
        redis_client.hmset(
            self.event_name,
            {
                "event_time": self.event_time,
                "event_place": self.event_place,
                "event_whole_capacity": event_whole_capacity
            }

        )
        redis_client.rpush(
            "list_of_events",
            self.event_name
        )


class Log_In:
    username = "events_manager"
    password = "manager_password"

    def __init__(self):
        pass

    @classmethod
    def manager_log_in(cls, userentry, passentry):
        cls.userentry = userentry
        cls.passentry = passentry
        if cls.userentry == cls.username and cls.passentry == cls.password:
            return True

    def add_event(self, us, ps, event_name, event_time, event_place, event_whole_capacity, event_price):
        self.us = us
        self.ps = ps
        if Log_In.manager_log_in(self.us, self.ps):
            self.event_name = event_name
            self.event_time = event_time
            self.event_place = event_place
            self.event_whole_capacity = event_whole_capacity
            self.event_price = event_price
            Event(self.event_name, self.event_time, self.event_place,
                  self.event_whole_capacity, self.event_price)

    @classmethod
    def costumer_log_in(self, id):
        self.id = id
        if re.search("[0-9]{10}", self.id):
            return True

    def show_events(self, id):
        self.id = id
        if Log_In.costumer_log_in(self.id):
            print(redis_client.lrange("list_of_events", 0, -1))

    def choose_event(self, id, event_choose, number_of_tickets):
        self.id = id
        self.event_choose = event_choose
        self.number_of_tickets = number_of_tickets
        if Log_In.costumer_log_in(self.id):


b = Log_In()

print(Log_In.costumer_log_in("1234512345"))
b.show_events("1234567891")


# print(Event.username)
# print(Event.log_in("events_manager", "manager_password"))
a = Log_In()

a.add_event("events_manager", "manager_password",
            "testoor", 'Jun 1 2005  1:33PM', 10, 10, 10)


**********************************
import re
from datetime import date, time, datetime
import redis
#redis_client = redis.Redis()
redis_client = redis.Redis(charset="utf-8", decode_responses=True)

class Payment:
	acount_info={1:[1:1000],2:[2:2000]}
	def __init__(self):
		pass
	@classmethod
	def pay(cls,pay_user,pay_pass,pay_amn):
		cls.pay_user=pay_user
		cls.pay_pass=pay_pass
		cls.pay_amn=pay_amn
		if Payment.acount_info[cls.pay_user][0]==cls.pay_pass and Payment.acount_info[cls.pay_user][1]>=cls.pay_amn:
			
			Payment.acount_info[cls.pay_user][1]=Payment.acount_info[cls.pay_user][1]-cls.pay_amn:
				return True


p=Payment()
	
class Event:
	

    # event time string should be like 'Jun 1 2005  1:33PM'

	discount_stu_code=1
	discount_admin_code=2
	discount_employe=3
	discount_ordinary_code=4

    def __init__(self, event_name, event_time, event_place, event_whole_capacity, event_price,event_remaining_capacity):
        self.event_name = event_name
        self.event_time = event_time
        self.event_place = event_place
        self.event_whole_capacity = event_whole_capacity
	self.remaining_capacity=self.event_whole_capacity
        self.event_price = event_price
	redis_client.hmset(
           dict_of_events
            {
                f"{self.event_name}:{self.event_time}:{self.event_place}:{self.event_whole_capacity}",
		f"{self.event_whole_capacity}:{self.event_price}:
            }

        )
	




        redis_client.hmset(
            self.event_name,
            {
                "event_time": self.event_time,
                "event_place": self.event_place,
                "event_whole_capacity": event_whole_capacity
		"self.event_remaining_capacity":self.event_whole_capacity
		"sold_ticket":0
            }

        )
        redis_client.rpush(
            "list_of_events",
            self.event_name
        )


class Log_In:
    username = "events_manager"
    password = "manager_password"

    def __init__(self):
        pass

    @classmethod
    def manager_log_in(cls, userentry, passentry):
        cls.userentry = userentry
        cls.passentry = passentry
        if cls.userentry == cls.username and cls.passentry == cls.password:
            return True

    def add_event(self, us, ps, event_name, event_time, event_place, event_whole_capacity, event_price):
        self.us = us
        self.ps = ps
        if Log_In.manager_log_in(self.us, self.ps):
            self.event_name = event_name
            self.event_time = event_time
            self.event_place = event_place
            self.event_whole_capacity = event_whole_capacity
            self.event_price = event_price
            Event(self.event_name, self.event_time, self.event_place,
                  self.event_whole_capacity, self.event_price)


    @classmethod
    def costumer_log_in(self, id):
        self.id = id
        if re.search("[0-9]{10}", self.id):
            return True

    def show_all_events_costumer(self, id):
        self.id = id
        if Log_In.costumer_log_in(self.id):
            print(redis_client.hgetall("dict_of_events"))


	def show_event_manager(self,us,ps,event_name):
	self.us = us
        self.ps = ps
	self.event_name=event_name
        if Log_In.manager_log_in(self.us, self.ps):
		print(hgetall(self.event_name))
			


	


    def choose_event(self, id, event_choose, number_of_tickets,pay_user,pay_pass):
	self.pay_user=pay_user
	self.pay_pass=pay_pass
	self.pay_amn=
        self.id = id
        self.event_choose = event_choose
        self.number_of_tickets = number_of_tickets
        if Log_In.costumer_log_in(self.id):
	cap_event_befor=hmget(self.event_choose):
	if cap_event_befor>= self.number_of_tickets and p.pay(self.pay_user,self.pay_pass,self.pay_amn)
		redis_client.hmset(
           dict_of_events
            {
                self.event_choose:{self.event_whole_capacity}:cap_event_befor-self.number_of_tickets
            }

        )
	        redis_client.hmset(
            self.event_name,
            {
                "event_time": self.event_time,
                "event_place": self.event_place,
                "event_whole_capacity": event_whole_capacity
		"self.event_remaining_capacity":self.event_whole_capacity bayad menhaye yek shavad
		"sold_ticket":bealaveye yek shavad
            }



	return f"{self.event_choose}:{self.number_of_tickets}:{self.id}:{self.pay_amn}"







		
		
	



b = Log_In()

print(Log_In.costumer_log_in("1234512345"))
b.show_events("1234567891")


# print(Event.username)
# print(Event.log_in("events_manager", "manager_password"))
a = Log_In()

a.add_event("events_manager", "manager_password",
            "testoor", 'Jun 1 2005  1:33PM', 10, 10, 10)

