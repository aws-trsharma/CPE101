import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_lower(self):
      list1 = ['h','e','l','l','o']
      self.assertTrue(is_lower_101(list1))
   def test_is_lower_101(self):
      list2 = ['b','R','O','T','h','e','r']
      self.assertFalse(is_lower_101(list2))
   def test_is_lower_101_2(self):
      list3 = ['h','r','v','d','l']
      self.assertTrue(is_lower_101(list3))
   def test_char_rot_13_1(self):
      char = "a"
      self.assertEqual(char_rot_13(char), "n")
   def test_char_rot_13_2(self):
      char = "m"
      self.assertEqual(char_rot_13(char), "z")
   def test_char_rot_13_3(self):
      char = "Z"
      self.assertEqual(char_rot_13(char), "M")
if __name__ == '__main__':
   unittest.main()

