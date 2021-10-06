import re
from datetime import date, time, datetime
import redis
import logging
redis_client = redis.Redis(charset="utf-8", decode_responses=True)
logging.basicConfig(filename='msg.log', filemode='a', level=logging.INFO)


class Payment:
    acounts_info = {1111111111: [1, 1000], 2222222222: [2, 2000]}

    def __init__(self):
        pass

    @classmethod
    def pay(cls, pay_user, pay_pass, pay_amn):
        cls.pay_user = pay_user
        cls.pay_pass = pay_pass
        cls.pay_amn = pay_amn
        try:
            if Payment.acounts_info[cls.pay_user][0] == cls.pay_pass and Payment.acounts_info[cls.pay_user][1] >= cls.pay_amn:
                Payment.acounts_info[cls.pay_user][1] = Payment.acounts_info[cls.pay_user][1]-cls.pay_amn
                return True
        except:
            pass
# this function help us separate data from redis valus that has the form of info1:info2:info3


def seperator(s, n):
    for i in range(n-1):
        s = s[s.index(r":")+1:]
    try:
        return s[:s.index(r":")]
    except:
        return s


class Event:
   # event time string should be like 'Jun 1 2005  1:33PM'

    discount_stu_code = [1, 2, 3]
    discount_admin_code = [4, 5, 6]
    discount_employee_code = [7, 8, 9]
    discount_ordinary_code = [10, 11, 12]
    stu_ids = ["1111111111", "2222222222"]
    admin_id = ["3333333333"]
    employe_ids = ["4444444444", "5555555555"]

    def __init__(self, event_name, event_time, event_place, event_whole_capacity, event_price):
        self.event_name = event_name
        self.event_time = event_time
        self.event_place = event_place
        self.event_whole_capacity = event_whole_capacity
        self.event_remaining_capacity = self.event_whole_capacity
        self.event_price = event_price
        redis_client.hset(
            "dict_of_events",
            f"{self.event_name}:{self.event_time}:{self.event_place}:{self.event_whole_capacity}",
            f"{self.event_remaining_capacity}:{self.event_price}"
        )
        logging.info(f"event {self.event_name} added at {datetime.now()}")

    #         redis_client.hmset(
    #             self.event_name,
    #             {
    #                 "event_time": self.event_time,
    #                 "event_place": self.event_place,
    #                 "event_whole_capacity": event_whole_capacity
    # 		"self.event_remaining_capacity":self.event_whole_capacity
    # 		"sold_ticket":0
    #             }

    #         )
    #         redis_client.rpush(
    #             "list_of_events",
    #             self.event_name
#     #         )


class Log_In:
    def __init__(self):
        self.username = "events_manager"
        self.password = "manager_password"

    def manager_log_in(self, userentry, passentry):
        self.userentry = userentry
        self.passentry = passentry
        if self.userentry == self.username and self.passentry == self.password:
            return True

    def add_event(self, us, ps, event_name, event_time, event_place, event_whole_capacity, event_price):
        self.us = us
        self.ps = ps
        if Log_In().manager_log_in(self.us, self.ps):
            self.event_name = event_name
            self.event_time = event_time
            self.event_place = event_place
            self.event_whole_capacity = event_whole_capacity
            self.event_price = event_price
            Event(self.event_name, self.event_time, self.event_place,
                  self.event_whole_capacity, self.event_price)


# a = Log_In()
# a.add_event("events_manager", "manager_password", "1", "1", "1", "1", "1")
# a.add_event("events_manager", "manager_password", "2", "2", "2", "2", "2")
# ^[1-9]\d{2}-\d{3}-\d{4}


    def costumer_log_in(self, id):
        self.id = id
        if re.search("^[0-9]{10}$", self.id):
            return True

    def show_all_events_costumer(self, id):
        self.id = id
        if Log_In().costumer_log_in(self.id):
            return redis_client.hgetall("dict_of_events")

# a=Log_In()
# print(a.show_all_events_costumer("1111111111"))

# 	def show_event_manager(self,us,ps,event_name):
# 	self.us = us
#         self.ps = ps
# 	self.event_name=event_name
#         if Log_In.manager_log_in(self.us, self.ps):
# 		print(hgetall(self.event_name))
# discount_stu_code = [1, 2, 3]
#     discount_admin_code = [4, 5, 6]
#     discount_employee_code = [7, 8, 9]
#     discount_ordinary_code = [10, 11, 12]
#     stu_ids = [1111111111, 2222222222]
#     admin_id = [3333333333]
#     employe_ids = [4444444444, 5555555555]

    def choose_event(self, id, event_choose, number_of_tickets, pay_user, pay_pass, discount_code="0"):
        self.id = id
        self.event_choose = event_choose
        self.number_of_tickets = number_of_tickets
        self.pay_user = pay_user
        self.pay_pass = pay_pass
        self.pay_amn = self.number_of_tickets * \
            int(seperator(redis_client.hget("dict_of_events", self.event_choose), 2))
        self.discount_code = discount_code
        if self.discount_code in Event.discount_stu_code and self.id in Event.stu_ids:
            print(self.discount_code in Event.discount_stu_code)
            self.pay_amn = self.pay_amn-20
            Event.discount_stu_code.remove(self.discount_code)
        if self.discount_code in Event.discount_admin_code and self.id in Event.admin_id:
            self.pay_amn = self.pay_amn-40
            Event.discount_admin_code.remove(self.discount_code)
        if self.discount_code in Event.discount_employee_code and self.id in Event.employe_ids:
            self.pay_amn = self.pay_amn-30
            Event.discount_employee_code.remove(self.discount_code)
        if self.discount_code in Event.discount_ordinary_code:
            self.pay_amn = self.pay_amn-15
            Event.discount_ordinary_code.remove(self.discount_code)

        if Log_In().costumer_log_in(self.id):
            cap_event_befor = int(seperator(redis_client.hget(
                "dict_of_events", self.event_choose), 1))
            if cap_event_befor >= self.number_of_tickets and Payment().pay(self.pay_user, self.pay_pass, self.pay_amn):
                s = str(cap_event_befor-self.number_of_tickets)+":" + \
                    seperator(redis_client.hget(
                        "dict_of_events", self.event_choose), 2)
                redis_client.hset(
                    "dict_of_events",
                    self.event_choose, s)
                logging.info(
                    f"{self.id} bougth {self.number_of_tickets} ticket for {self.event_choose} at {datetime.now}")


#         redis_client.hmset(
#         self.event_name,
#         {
#             "event_time": self.event_time,
#             "event_place": self.event_place,
#             "event_whole_capacity": event_whole_capacity
# 	"self.event_remaining_capacity":self.event_whole_capacity bayad menhaye yek shavad
# 	"sold_ticket":bealaveye yek shavad
# }
# return f"{self.event_choose}:{self.number_of_tickets}:{self.id}:{self.pay_amn}"
a = Log_In()
a.add_event("events_manager", "manager_password", "1", "1", "1", "40", "100")
a.add_event("events_manager", "manager_password", "2", "2", "2", "20", "200")
a.choose_event("1111111111", "1:1:1:40", 2, 1111111111, 1, 1)
print(Payment.acounts_info)


# b = Log_In()

# print(Log_In.costumer_log_in("1234512345"))
# b.show_events("1234567891")

# # print(Event.username)
# # print(Event.log_in("events_manager", "manager_password"))
# a = Log_In()

# a.add_event("events_manager", "manager_password",
#             "testoor", 'Jun 1 2005  1:33PM', 10, 10, 10)
