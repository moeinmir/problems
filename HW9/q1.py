class Ticket:
    travel_cost=100
    def __init__(self,credit):
        self.credit=credit
    def travel(self):
        if self.credit>Ticket.travel_cost:
            self.credit=self.credit-Ticket.travel_cost
        else:
            print("your credit is not enoough")


class one_way(Ticket)
    



a=Ticket(1000)
a.travel()
print(a.credit)

    