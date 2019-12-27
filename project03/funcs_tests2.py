import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
      
  def test_check_rows0(self):
      puzzle = []
      puzzle.append([1,2,3,3,5])
      puzzle.append([2,4,1,3,5])
      puzzle.append([0,0,0,0,0])
      puzzle.append([0,0,0,0,0])
      puzzle.append([0,0,0,0,0])
      self.assertFalse(check_rows_valid(puzzle))
  def test_check_columns0(self):
     puzzle= []
     puzzle.append([1,5,0,0,0])
     puzzle.append([2,4,0,0,0])
     puzzle.append([3,3,0,0,0])
     puzzle.append([4,2,0,0,0])
     puzzle.append([5,1,0,0,0])
     self.assertTrue(check_columns_valid(puzzle))
  def test_check_cages_0(self):
     puzzle = []
     puzzle.append([5,1,2,3,4])
     puzzle.append([0,2,3,4,5])
     puzzle.append([2,3,0,5,1])
     puzzle.append([3,0,0,1,2])
     puzzle.append([0,0,0,0,0,])
     cages = []
     cages.append([6,3,0,5,1])
     cages.append([7,3,2,6,7])
     cages.append([9,2,4,9])
     self.assertFalse(check_valid(puzzle,cages))
  def test_check_cages_1(self):
     puzzle = []
     puzzle.append([5,1,2,3,4])
     puzzle.append([1,2,3,4,5])
     puzzle.append([2,3,0,5,1])
     puzzle.append([3,0,0,1,2])
     puzzle.append([0,0,0,0,0])
     cages = []
     cages.append([8, 2, 15, 20])
     cages.append([7,3,2,6,7])
     cages.append([9,2,4,4])
     self.assertFalse(check_valid(puzzle,cages))
  def test_check_cages_2(self):
     puzzle = []
     puzzle.append([1,2,3,4,5])
     puzzle.append([5,1,2,3,4])
     puzzle.append([2,3,4,5,1])
     puzzle.append([3,4,5,1,2])
     puzzle.append([4,5,1,2,3])
     cages = []
     cages.append([10, 3, 4, 8,7])
     cages.append([5,2,15,10])
     cages.append([9, 2, 20, 21])
     self.assertTrue(check_valid(puzzle, cages))
  def test_check_cages_3(self):
     puzzle = []
     puzzle.append([3,5,2,1,4])
     puzzle.append([5,0,3,4,2])
     puzzle.append([2,4,1,5,3])
     puzzle.append([1,2,4,3,5])
     puzzle.append([4,3,5,2,1])
     cages = []
     cages.append([9,3,20,22,6])
     cages.append([7,2,1,2])
     cages.append([10,3,3,8,13])
     cages.append([3,1,7])
     cages.append([8,3,10,11,16])
     self.assertFalse(check_valid(puzzle, cages))
  def test_check_cages_4(self):
     puzzle = []
     puzzle.append([1,4,5,1,2])
     cages = []
     cages.append([9,3,0,1,2])
     self.assertFalse(check_valid(puzzle, cages))
if __name__ == '__main__':
   unittest.main()
          
