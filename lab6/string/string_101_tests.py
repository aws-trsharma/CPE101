import unittest
from string_101 import *

class TestString(unittest.TestCase):
 def test_lower(self):
      str = "hello"
      ans = "uryyb"
      self.assertEqual(str_rot_13(str), ans)
 def test_lower_2(self):
      str = "abmnoz"
      ans = "nozabm"
      self.assertEqual(str_rot_13(str), ans)
 def test_lower_1(self):
      str = "%%5a"
      ans = "%%5n"
      self.assertEqual(str_rot_13(str), ans)
 def str_translate_101_1(self):
      str = "abcdcba"
      self.assertListEqual(str_translate_101(str, "a", "x"), "xbcdcbx")
 def str_translate_101_2(self):
      str = "hello"
      self.assertListEqual(str_translate_101(str, "e", "u"), "hullo")
if __name__ == '__main__':
   unittest.main()

