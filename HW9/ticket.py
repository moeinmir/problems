from datetime import date, timedelta
class Ticket:
    travel_cost = 100
    def __init__(self, credit):
        self.credit = credit
    def travel(self):
        if self.credit >= Ticket.travel_cost:
            self.credit = self.credit-Ticket.travel_cost
        else:
            print("your credit is not enoough")
class OneWay(Ticket):
    def __init__(self):
        self.credit = Ticket.travel_cost

    def travel(self):
        if self.credit >= Ticket.travel_cost:
            self.credit = self.credit-Ticket.travel_cost
        else:
            print("your ticket already has been used")


class ChargeAble(Ticket):
    travel_cost = 90

    def travel(self):
        if self.credit >= ChargeAble.travel_cost:
            self.credit = self.credit-ChargeAble.travel_cost
        else:
            print("your credit is not enoough")

    def charge(self, charge_amount):
        self.charge_amount = charge_amount
        self.credit += charge_amount


class ChargeAbleTimeLimit(ChargeAble):
    extention_fee = 50
    travel_cost = 80

    def __init__(self, credit, time_limit):
        super().__init__(credit)
        time_tuple = tuple(map(int, time_limit.split()))
        self.time_limit = date(time_tuple[0], time_tuple[1], time_tuple[2])

    def travel(self):
        if date.today() > self.time_limit:
            print("you should extend your ticket")
        elif self.credit >= ChargeAbleTimeLimit.travel_cost:
            self.credit = self.credit-ChargeAbleTimeLimit.travel_cost
        else:
            print("your credit is not enough")


# this function is suposed to extend the time limit for number_of_mounth and reduce the credit in exchange

    def extend(self, number_of_mounth):
        self.number_of_mounth = number_of_mounth
        if self.credit >= self.number_of_mounth*ChargeAbleTimeLimit.extention_fee:
            self.credit = self.credit-ChargeAbleTimeLimit.extention_fee*self.number_of_mounth
            self.time_limit = self.time_limit + \
                timedelta(days=self.number_of_mounth*30)
        else:
            print(
                "your credit is not enough for extention you have to charge your acount first")
