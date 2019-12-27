import unittest
import filter

class TestCases(unittest.TestCase):
   def test_are_positive(self):
      # Add code here.
      filter1 = [5,-7,3,-2,-1,5]
      filter2 = filter.are_positive(filter1)
      self.assertListEqual(filter2, [5,3,5])
   def test_are_positive_1(self):
      filter1 = [-7, 99, 2, 33, -1, 15]
      filter2 = filter.are_positive(filter1)
      self.assertListEqual(filter2, [99,2,33,15])
   def test_are_greater_than_n(self):
      filter1 = [15, 10, 0, 2, 3, 13]
      filter2 = filter.are_greater_than_n(5,filter1)
      self.assertListEqual(filter2, [15, 10, 13])
   def test_are_greater_than_n_1(self):
      filter1 = [76, 75,73, 72 ,71]
      filter2 = filter.are_greater_than_n(73, filter1)
      self.assertListEqual(filter2, [76, 75])
   def test_are_divisbile_by_n(self):
      filter1 = [30,31,32,33,34,35,36]
      filter2 = filter.are_divisible_by_n(2, filter1)
      self.assertListEqual(filter2, [30, 32, 34, 36])
   def test_are_divisible_by_n_1(self):
      filter1 = [15,21,25,29,30, 34,35,39,40,44,45,49,50]
      filter2 = filter.are_divisible_by_n(5,filter1)
      self.assertListEqual(filter2, [15, 25, 30, 35, 40, 45, 50])
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

