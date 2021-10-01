import unittest
from acount import Acount


class TestAcount(unittest.TestCase):

    def setUp(self):
        print(1)
        self.a = Acount(1, 1000)
        self.b = Acount(2, 1500)

    def test_transfer(self):
        print(1)
        self.a.transfer(1, 2, 500)
        self.assertEqual(self.a.list_of_client[1].acn_bln, 500)

    def test_trans(self):
        self.assertEqual(len(self.a.list_of_client, 2))

    def test_membership(self):
        self.assertIn(Acount.list_of_client[1], self.a.list_of_client)
        self.assertTrue(Acount.list_of_client[1], Acount.list_of_client)


if __name__ == "__main__":
    unittest.main()
