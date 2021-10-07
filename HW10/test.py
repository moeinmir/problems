import unittest
import re
from datetime import datetime
import redis
from q1 import *


class TestStudentMethods(unittest.TestCase):
    def setUp(self):
        redis_client = redis.Redis(charset="utf-8", decode_responses=True)

    def test_bankacount(self):
        BankAcount("1111111111", "1", "1000000")
        balance = redis_client.hget("acounts_info", "1111111111")
        self.assertIsNotNone(balance)
        self.assertEqual(seperator(balance, 2), "1000000")

    def test_pay(self):
        pay("1111111111", "1", "100000")
        self.assertEqual(seperator(redis_client.hget(
            "acounts_info", "1111111111"), 2), str(1000000-100000))

    def test_discounts(self):
        Discounts("student", "1123")
        self.assertIn("1123", redis_client.lrange(
            "students_discount_codes", 0, -1))

    def test_log_in(self):
        Log_In("2222222222", "password")
        self.assertEqual(redis_client.hget(
            "manager_user_pass", "username"), "2222222222")
        self.assertEqual(redis_client.hget(
            "manager_user_pass", "password"), "password")
        self.assertEqual(manager_log_in("2222222222", "password"), True)

    def test_add_event(self):
        add_event("2222222222", "password", "konserteshajar",
                  "aban", "vahdat", "200", "50000")
        self.assertEqual(redis_client.hget("dict_of_events",
                         "konserteshajar:aban:vahdat:200"), "200:50000")

    def test_costumer_log_in(self):
        costumer_log_in("2150008394", "student")
        self.assertEqual(redis_client.get("2150008394"), "student")

    def test_show_all_events_costumer(self):
        self.assertIsNotNone(show_all_events_costumer("2150008394"))

    def test_show_event_manager(self):
        self.assertIsNotNone(show_event_manager(
            "2222222222", "password", "konserteshajar"))

    def test_choose_event(self):
        BankAcount("2150008394", "2", "2000000")
        cap_before = seperator(redis_client.hget("dict_of_events",
                                                 "konserteshajar:aban:vahdat:200"), 1)
        choose_event("2150008394", "konserteshajar:aban:vahdat:200",
                     "2", "2150008394", "2", "1123")
        self.assertEqual(seperator(redis_client.hget("dict_of_events",
                                                     "konserteshajar:aban:vahdat:200"), 1), str(int(cap_before)-2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
