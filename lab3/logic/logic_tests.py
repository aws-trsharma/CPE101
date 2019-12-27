import unittest
from logic import *

class TestCases(unittest.TestCase):
    def test_is_even1(self):
       self.assertEqual(is_even(0), True)
    def test_is_even2(self):
       self.assertEqual(is_even(11), False)
    def test_is_even3(self):
       self.assertEqual(is_even(10), True)
    def test_in_an_interval_1(self):
        self.assertEqual(in_an_interval(110), False)
    def test_in_an_interval_2(self):
        self.assertEqual(in_an_interval(5), True)
    def test_in_an_interval_3(self):
        self.assertEqual(in_an_interval(47), False)
    def test_in_an_interval_4(self):
        self.assertEqual(in_an_interval(12), False)
    def test_in_an_interval_5(self):
        self.assertEqual(in_an_interval(103), True)
     

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

