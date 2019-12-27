import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality(self):
      # Add test here
      p1 = Point(5,3)
      p2 = Point(5,3)
      self.assertEqual(p1, p2)
   def test_equality_1(self):
      p1 = Point(2,9)
      p2 = Point(5,9)
      self.assertNotEqual(p1,p2)
   def test_equality_3(self):
      p1 = Point(2.0000000000000000001, 9)
      p2 = Point(2, 9)
      self.assertEqual(p1,p2)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

