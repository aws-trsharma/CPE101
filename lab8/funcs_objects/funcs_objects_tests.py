import unittest
from objects import *
from funcs_objects import *
class TestCases(unittest.TestCase):
   def test_point(self):
      # Add code here.
      p1 = Point(5,3)
      self.assertEqual(p1.x,5)
      self.assertEqual(p1.y,3)


   def test_circle(self):
      # Add code here.
      c1 = Circle(Point(1,3), 4)
      self.assertEqual(c1.center.x, 1)
      self.assertEqual(c1.center.y,3)
      self.assertEqual(c1.radius, 4)

   def test_distance_1(self):
       p1 = Point(5,3)
       p2 = Point(9,6)
       self.assertEqual(distance(p1,p2), 5)

   def test_distance_2(self):
       p1 = Point(2,3)
       p2 = Point(9,9)
       self.assertAlmostEqual(distance(p1,p2), 9.21954445729887)

   def test_circle_1(self):
       c1 = Circle(Point(3,4), 5)
       c2 = Circle(Point(14,18), 8)
       self.assertFalse(circles_overlap(c1, c2))

   def test_circle_2(self):
       c1 = Circle(Point(-10,8), 30)
       c2 = Circle(Point(14,-24),10)
       self.assertTrue(circles_overlap(c1, c2))
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

