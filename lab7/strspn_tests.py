import unittest
from strspn import *

class TestCases(unittest.TestCase):
    def test_my_strspn_01(self):
        self.assertEqual(3, my_strspn("calpoly", "local"))
    def test_my_strspn_02(self):
        self.assertEqual(3, my_strspn("calpoly", "california"))
    def test_my_strspn_03(self):
        self.assertEqual(4, my_strspn("calpoly", "place"))
    def test_my_strspn_04(self):
        self.assertEqual(4, my_strspn("cccca", "office"))
    def test_my_strspn_05(self):
        self.assertEqual(5, my_strspn("minute", "simulation"))
    def test_my_strspn_06(self):
        self.assertEqual(0, my_strspn("",""))
    def test_my_strspn_07(self):
        self.assertEqual(0, my_strspn("","blahblahblah"))
    def test_my_strspn_08(self):
        self.assertEqual(12, my_strspn("blahblahblah", "blahblahblah"))
    def test_my_strspn_09(self):
        self.assertEqual(4, my_strspn("blah", "blahblahblah"))
    def test_my_strspn_10(self):
        self.assertEqual(1, my_strspn("b", "b"))
if __name__ == '__main__':
   unittest.main()
