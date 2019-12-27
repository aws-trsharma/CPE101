import unittest
from conditional import *

class TestCases(unittest.TestCase):
   
      
     def test_max_101(self):
      self.assertEqual(max_101(15,10),15)
     def test_max_101_1(self):
      self.assertEqual(max_101(75,100), 100)
     def test_max_101_2(self):
      self.assertEqual(max_101(30,30),30)
     def test_max_of_three(self):
      self.assertEqual(max_of_three(30.5,17.5,12.5), 30.5)
     def test_max_of_three_1(self):
      self.assertEqual(max_of_three(109.3, 115.7,12.7),115.7)
     def test_max_of_three_1(self):
      self.assertEqual(max_of_three(3,3,1),3)
     def test_max_of_three_2(self):
      self.assertEqual(max_of_three(0.5, 19.0, 145.6), 145.6)
     def test_rental_late_fee(self):
      self.assertEqual(rental_late_fee(0), 0)
     def test_rental_late_fee_1(self):
      self.assertEqual(rental_late_fee(8), 5)
     def test_rental_late_fee_2(self):
      self.assertEqual(rental_late_fee(13),7)
     def test_rental_late_fee_3(self):
      self.assertEqual(rental_late_fee(24), 19)
     def test_rental_late_fee_4(self):
      self.assertEqual(rental_late_fee(45), 100)
     ##  max_of_three(0, 0, 0)
      ##  rental_late_fee(0)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

