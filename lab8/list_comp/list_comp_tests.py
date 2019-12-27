import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
    def test_distance_all_1(self):
       list1 = [Point(5,3), Point(4,6),Point(7,1), Point(8,2), Point(9,1)]
       list2 = [5.83095189484, 7.211102550, 7.071067811, 8.246211251, 9.0553851281]
       self.assertListAlmostEqual(distance_all(list1), list2)
    def test_distance_all_2(self):
       list1 = [Point(2,1), Point(3,5), Point(4,5), Point(6,1)]
       list2 = [2.236067977,5.83095189,6.4031242, 6.0827625]
       self.assertListAlmostEqual(distance_all(list1), list2)
    def test_are_in_first_quadrant_1(self):
       list1 = [Point(2,3), Point(-1,5), Point(2,2), Point(-2,-2)]
       list2 = [Point(2,3), Point(2,2)]
       self.assertListEqual(are_in_first_quadrant(list1), list2)
    def test_are_in_first_quadrant_2(self):
        list1 = [Point(-1,-1), Point(2,2), Point(0,0), Point(4,-4)]
        list2 = [Point(2,2)]
        self.assertListEqual(are_in_first_quadrant(list1), list2)
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip (l1, l2):
            self.assertAlmostEqual(el1,el2)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

