import unittest
from groups import *


class TestCases(unittest.TestCase):
     def test_groups_of_3(self):
        list1 = [1,2,3,4,5,6,7,8,9]
        list2 = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertListEqual(groups_of_3(list1), list2)
     def test_groups_of_3_1(self):
        list1 = [1,2,3,4,5,6,7,8]
        list2 = [[1,2,3],[4,5,6],[7,8]]
        self.assertListEqual(groups_of_3(list1), list2)
     def test_groups_of_3_2(self):
        list1 = [1,2,3,4,5,6,7,8,9,10]
        list2 = [[1,2,3], [4,5,6], [7,8,9], [10]]
        self.assertListEqual(groups_of_3(list1), list2)
if __name__ == '__main__':
   unittest.main()
