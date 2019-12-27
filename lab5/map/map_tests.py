import unittest
import map

class TestCases(unittest.TestCase):
   def test_square_all(self):
      # Add code here.
      list1 = [2,3,4,5]
      list2 = map.square_all(list1)
      self.assertListEqual(list2, [4, 9, 16, 25]) 
   def test_square_all_2(self):
      list1 = [4,3,2,1]
      list2 = map.square_all(list1)
      self.assertListEqual(list2, [16, 9, 4, 1])
   def test_add_n_all(self):
      list1 = [2, 4, 6, 8]
      list2 = map.add_n_all(5, list1)
      self.assertListEqual(list2, [7, 9, 11, 13])
   def test_add_n_all_2(self):
      list1 = [9, 7, 1, 3]
      list2 = map.add_n_all(6, list1)
      self.assertListEqual(list2, [15, 13, 7, 9])
   def test_even_or_odd_all(self):
      list1 = [2,5,6,7]
      list2 = map.even_or_odd_all(list1)
      self.assertListEqual(list2, [True, False, True, False])
   def test_even_or_odd_all_2(self):
      list1 = [9,4,2,3]
      list2 = map.even_or_odd_all(list1) 
      self.assertListEqual(list2, [False, True, True, False])
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

