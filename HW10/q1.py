import re
from datetime import datetime
import redis
import logging
redis_client = redis.Redis(charset="utf-8", decode_responses=True)
logging.basicConfig(filename='msg.log', filemode='a', level=logging.INFO)


class BankAcount:
    def __init__(self, id, password, balance):
        self.id = id
        self.password = password
        self.balance = balance
        redis_client.hset("acounts_info",
                          f"{self.id}",
                          f"{self.password}:{self.balance}"
                          )


def seperator(s, n):
    for i in range(n-1):
        s = s[s.index(r":")+1:]
    try:
        return s[:s.index(r":")]
    except:
        return s


def pay(pay_user, pay_pass, pay_amn):
    try:
        if seperator(redis_client.hget("acounts_info", pay_user), 1) == pay_pass and\
                int(seperator(redis_client.hget("acounts_info", pay_user), 2)) >= int(pay_amn):
            redis_client.hset("acounts_info", pay_user, str(
                pay_pass)+":"+str(int(seperator(redis_client.hget("acounts_info", pay_user), 2))-int(pay_amn)))
            return True
    except:
        logging.error(f"wrong entry for payment at {datetime.now()}")


class Discounts:
    def __init__(self, discount_type=None, discount_code=None):
        self.discount_type = discount_type
        self.discount_code = discount_code
        if self.discount_type == "student":
            redis_client.rpush("students_discount_codes", self.discount_code)
        if self.discount_type == "admin":
            redis_client.rpush("admin_discount_codes", self.discount_code)
        if self.discount_type == "employee":
            redis_client.rpush("employee_discount_codes", self.discount_code)
        if self.discount_type == "ordinary":
            redis_client.rpush("ordinary_discount_codes", self.discount_code)
        else:
            logging.error(
                f"wrong entry for discount code adding at {datetime.now()}")


class Event:

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
# in this part we could put mor enformation for each event and it is for manager
        redis_client.hset(
            self.event_name,
            "event_time", self.event_time)
        redis_client.hset(
            self.event_name,
            "event_place", self.event_place)
        redis_client.hset(
            self.event_name,
            "event_whole_capacity", self.event_whole_capacity)
        redis_client.hset(
            self.event_name,
            "event_remaining_capacity", self.event_whole_capacity)
        redis_client.hset(
            self.event_name,
            "sold_ticket", "0"
        )


class Log_In:
    def __init__(self, username="events_manager", password="manager_password"):
        self.username = username
        self.password = password
        redis_client.hset("manager_user_pass",
                          "username",
                          self.username)
        redis_client.hset("manager_user_pass",
                          "password",
                          self.password)


def manager_log_in(userentry, passentry):
    if userentry == redis_client.hget("manager_user_pass", "username") and\
            passentry == redis_client.hget("manager_user_pass", "password"):
        logging.info(f"manager entered at {datetime.now()}")
        return True

    else:
        logging.error(f"manager enter wronge user pass at {datetime.now()}")


def add_event(us, ps, event_name, event_time, event_place, event_whole_capacity, event_price):
    if manager_log_in(us, ps):
        Event(event_name, event_time, event_place,
              event_whole_capacity, event_price)


def costumer_log_in(id, personal_type="ordinary"):
    if re.search("^[0-9]{10}$", id):
        a = True
        logging.info(f"{id} entered at {datetime.now()}")
        if personal_type != "ordinary":
            if personal_type == "student":
                redis_client.set(id, "student")
            if personal_type == "admin":
                redis_client.set(id, "admin")
            if personal_type == "employee":
                redis_client.set(id, "employee")
            else:
                logging.error(
                    f"wronge entry for personality at {datetime.now()}")
        else:
            redis_client.set(id, "ordinary")
    else:
        a = False
        logging.error(f"wronge entry for id at {datetime.now()}")
    return a


def show_all_events_costumer(id):
    if costumer_log_in(id):
        return redis_client.hgetall("dict_of_events")


def show_event_manager(us, ps, event_name):
    if manager_log_in(us, ps):
        logging.info(f"manger saw {event_name} at {datetime.now()}")
        return redis_client.hgetall(event_name)
    else:
        logging.error(f"manager entered wrong entry at {datetime.now()}")


def choose_event(id, event_choose, number_of_tickets, pay_user, pay_pass, discount_code="0"):
    cap_event_befor = int(seperator(redis_client.hget(
        "dict_of_events", event_choose), 1))
    pay_amn = int(number_of_tickets) * \
        int(seperator(redis_client.hget("dict_of_events", event_choose), 2))
    if discount_code in redis_client.lrange("students_discount_codes", 0, -1) and redis_client.get(id) == "student":
        pay_amn = pay_amn-20
        if int(cap_event_befor) >= int(number_of_tickets):
            if pay(pay_user, pay_pass, pay_amn):
                s = str(int(cap_event_befor)-int(number_of_tickets))+":" + \
                    seperator(redis_client.hget(
                        "dict_of_events", event_choose), 2)
                redis_client.hset(
                    "dict_of_events",
                    event_choose, s)
                redis_client.lrem("students_discount_codes", 1, discount_code)
                redis_client.hset(seperator(event_choose, 1), "sold_ticket", str(
                    int(redis_client.hget(seperator(event_choose, 1), "sold_ticket"))+1))
                redis_client.hset(seperator(event_choose, 1), "event_remaining_capacity", str(
                    int(redis_client.hget(seperator(event_choose, 1), "event_remaining_capacity"))-1))
                logging.info(
                    f"{id} bougth {number_of_tickets} ticket for {event_choose} at {datetime.now()}")
                return f"{event_choose}:{number_of_tickets}:{id}:{pay_amn}"
    elif discount_code in redis_client.lrange("admin_discount_codes", 0, -1) and redis_client.get(id) == "admin":
        pay_amn = pay_amn-40
        if int(cap_event_befor) >= int(number_of_tickets):
            if pay(pay_user, pay_pass, pay_amn):
                s = str(int(cap_event_befor)-int(number_of_tickets))+":" + \
                    seperator(redis_client.hget(
                        "dict_of_events", event_choose), 2)
                redis_client.hset(
                    "dict_of_events",
                    event_choose, s)
                redis_client.lrem("admin_discount_codes", 1, discount_code)
                redis_client.hset(seperator(event_choose, 1), "sold_ticket", str(
                    int(redis_client.hget(seperator(event_choose, 1), "sold_ticket"))+1))
                redis_client.hset(seperator(event_choose, 1), "event_remaining_capacity", str(
                    int(redis_client.hget(seperator(event_choose, 1), "event_remaining_capacity"))-1))
                logging.info(
                    f"{id} bougth {number_of_tickets} ticket for {event_choose} at {datetime.now()}")
                return f"{event_choose}:{number_of_tickets}:{id}:{pay_amn}"
    elif discount_code in redis_client.lrange("employee_discount_codes", 0, -1) and redis_client.get(id) == "employee":
        pay_amn = pay_amn-30
        if int(cap_event_befor) >= int(number_of_tickets):
            if pay(pay_user, pay_pass, pay_amn):
                s = str(int(cap_event_befor)-int(number_of_tickets))+":" + \
                    seperator(redis_client.hget(
                        "dict_of_events", event_choose), 2)
                redis_client.hset(
                    "dict_of_events",
                    event_choose, s)
                redis_client.lrem(
                    "employee_discount_codes", 1, discount_code)
                redis_client.hset(seperator(event_choose, 1), "sold_ticket", str(
                    int(redis_client.hget(seperator(event_choose, 1), "sold_ticket"))+1))
                redis_client.hset(seperator(event_choose, 1), "event_remaining_capacity", str(
                    int(redis_client.hget(seperator(event_choose, 1), "event_remaining_capacity"))-1))
                logging.info(
                    f"{id} bougth {number_of_tickets} ticket for {event_choose} at {datetime.now()}")
                return f"{event_choose}:{number_of_tickets}:{id}:{pay_amn}"
    elif discount_code in redis_client.lrange("ordinary_discount_codes", 0, -1):
        pay_amn = pay_amn-15
        if int(cap_event_befor) >= int(number_of_tickets):
            if pay(pay_user, pay_pass, pay_amn):
                s = str(int(cap_event_befor)-int(number_of_tickets))+":" + \
                    seperator(redis_client.hget(
                        "dict_of_events", event_choose), 2)
                redis_client.hset(
                    "dict_of_events",
                    event_choose, s)
                redis_client.lrem(
                    "ordinary_discount_codes", 1, discount_code)
                redis_client.hset(seperator(event_choose, 1), "sold_ticket", str(
                    int(redis_client.hget(seperator(event_choose, 1), "sold_ticket"))+1))
                redis_client.hset(seperator(event_choose, 1), "event_remaining_capacity", str(
                    int(redis_client.hget(seperator(event_choose, 1), "event_remaining_capacity"))-1))
                logging.info(
                    f"{id} bougth {number_of_tickets} ticket for {event_choose} at {datetime.now()}")
                return f"{event_choose}:{number_of_tickets}:{id}:{pay_amn}"
    else:
        if int(cap_event_befor) >= int(number_of_tickets):
            if pay(pay_user, pay_pass, pay_amn):
                s = str(int(cap_event_befor)-int(number_of_tickets))+":" + \
                    seperator(redis_client.hget(
                        "dict_of_events", event_choose), 2)
                redis_client.hset(
                    "dict_of_events",
                    event_choose, s)
                redis_client.hset(seperator(event_choose, 1), "sold_ticket", str(
                    int(redis_client.hget(seperator(event_choose, 1), "sold_ticket"))+1))
                redis_client.hset(seperator(event_choose, 1), "event_remaining_capacity", str(
                    int(redis_client.hget(seperator(event_choose, 1), "event_remaining_capacity"))-1))

                logging.info(
                    f"{id} bougth {number_of_tickets} ticket for {event_choose} at {datetime.now()}")
                return f"{event_choose}:{number_of_tickets}:{id}:{pay_amn}"
