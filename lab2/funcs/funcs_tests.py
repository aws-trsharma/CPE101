import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here. REMOVE PASS
      self.assertEqual(funcs.f(2),32)
      
   def test_f_2(self):
      self.assertEqual(funcs.f(5), 185)
  
   def test_g_1(self):
      # Add code here. REMOVE PASS
      self.assertRaises(ZeroDivisionError, funcs.g, 0, 3)

   def test_g_2(self):
     #2nd gtest check
     self.assertEqual(funcs.g (3,3),2)

   def test_hypotenuse_1(self):
     self.assertEqual(funcs.hypotenuse(3,4),5)

   def test_hypotenuse_2(self):
     self.assertAlmostEqual(funcs.hypotenuse(5,10),11.18033989)

   def test_is_positive_1(self):
     self.assertTrue(funcs.is_positive(10))

   def test_is_positive_2(self):
     self.assertFalse(funcs.is_positive(0))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

