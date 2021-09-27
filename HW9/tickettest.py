from ticket import *
import unittest


class TicketTest(unittest.TestCase):
    def setUp(self):
        self.var_one_way = OneWay()
        self.var_chargeable = ChargeAble(10000)
        self.var_chargeable_time_limit = ChargeAbleTimeLimit(
            10000, "2022 11 11")

    def test_travel(self):
        # test for one way travel
        self.var_one_way.travel()
        self.assertEqual(self.var_one_way.credit, 0)
        # one way ticket credit has came to zero after one use
        self.var_one_way.travel()
        self.assertEqual(self.var_one_way.credit, 0)
        self.var_one_way.travel()
        self.assertEqual(self.var_one_way.credit, 0)
        # one way ticket credit has not changed after one use and it is useless after this
        # test for chargeable
        self.befor_chargeable = self.var_chargeable.credit
        for i in range(5):
            self.var_chargeable.travel()
            self.assertEqual(self.var_chargeable.credit,
                             self.befor_chargeable-(i+1)*ChargeAble.travel_cost)
        # test for charge able time limit
            self.befor_chargeable_time_limit = self.var_chargeable_time_limit.credit
        for i in range(5):
            self.var_chargeable_time_limit.travel()
            self.assertEqual(self.var_chargeable_time_limit.credit,
                             self.befor_chargeable_time_limit-(i+1)*ChargeAbleTimeLimit.travel_cost)

        def test_charg(self):
            # charge test for chargeable
            self.befor_chargeable = self.var_chargeable.credit
            for i in range(5):
                self.var_chargeable.charge(500)
                self.assertEqual(self.var_chargeable.credit,
                                 self.befor_chargeable+(i+1)*500)
            # chage test for chargeable time limit
            self.befor_chargeable_time_limit = self.var_chargeable_time_limit.credit
            for i in range(5):
                self.var_chargeable_time_limit.charge(500)
                self.assertEqual(self.var_chargeable_time_limit.credit,
                                 self.befor_chargeable_time_limit+(i+1)*500)

        def test_extend(self):
            self.befor_time_limit = self.var_chargeable_time_limit.time_limit
            for i in range(a):
                self.var_chargeable_time_limit.extend(1)
                self.assertEqual(self.var_chargeable_time_limit.time_limit,
                                 self.befor_time_limit+(i+1)*timedelta(days=30))


if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
