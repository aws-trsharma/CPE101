import unittest
import poly

class TestPoly(unittest.TestCase):
   def test_poly1(self):
    poly1 = [2.3, 4.7, 1.0]
    poly2 = [1.2, 2.1, -3.2]

    poly3 = poly.poly_add2(poly1, poly2)
    self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])
   def test_poly2(self):
    poly1 = [5.1, 1.5, 0]
    poly2  = [-2.5, 3.7,-2.5]

    poly3 = poly.poly_add2(poly1, poly2)
    self.assertListAlmostEqual(poly3, [2.6, 5.2, -2.5])
   def test_poly3(self):
    poly1 = [5, 2, -5]
    poly2 = [3, 2, 2]
    
    poly3 = poly.poly_mult2(poly1, poly2)
    self.assertListAlmostEqual(poly3, [15, 16,-1, -6, -10])
   def test_poly4(self):
    poly1 = [8,5,-4]
    poly2 = [3,7,-9]

    poly3 = poly.poly_mult2(poly1, poly2)
    self.assertListAlmostEqual(poly3, [24, 71, -49, -73, 36])
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   # Add tests here

if __name__ == '__main__':
   unittest.main()
