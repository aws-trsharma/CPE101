import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_1(self):
      sum1 = [10,15,20,23,24]
      self.assertEqual(sum(sum1),92)
   def test_sum_2(self):
      sum1 = [-10, -5, -3, 10 ,13]
      self.assertEqual(sum(sum1),5)
   def test_sum_3(self):
      sum1 = [0,0,0,0,19]
      self.assertEqual(sum(sum1), 19)
   def test_index_of_smallest_1(self):
      list1 = [6,7,8,9,5,10,5]
      self.assertEqual(index_of_smallest(list1),4)
   def test_index_of_smallest_2(self):
      list1 = []
      self.assertEqual(index_of_smallest(list1), -1)
   def test_index_of_smallest_3(self):
      list1 = [5,6,7,8,2,10]
      self.assertEqual(index_of_smallest(list1), 4)
   def test_index_of_smallest_4(self):
      list1 = [2,3,4,5,6,7]
      self.assertEqual(index_of_smallest(list1), 0)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

