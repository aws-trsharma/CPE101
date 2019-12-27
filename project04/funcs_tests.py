import unittest
from funcs import *
class TestCases(unittest.TestCase):
    def test_check_rows0(self):
      puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
      val = puzzle_to_lists(puzzle)
      self.assertListEqual(checkRows(val, "UNIX"), [9,3])
    def test_check_rows1(self):
      puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
      val = puzzle_to_lists(puzzle)
      self.assertFalse(checkRows(val, "VROW"))
    def test_check_columns1(self):
      puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
      val = puzzle_to_lists(puzzle)
      self.assertListEqual(checkColumns(val, "CALPOLY"), [1,0])
    def test_check_columns2(self):
      puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
      val = puzzle_to_lists(puzzle)
      self.assertFalse(checkColumns(val, "BROWDYM"))
    def test_check_columnBackward0(self):
      puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
      val = puzzle_to_lists(puzzle)
      self.assertListEqual(checkColumnsBackwards(val, "DLWI"), [4,3])
    def test_check_columnBackward1(self):
      puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
      val = puzzle_to_lists(puzzle)
      self.assertFalse(checkColumnsBackwards(val, "YOOOOOOO"))
    def test_check_Row_Backwards(self): 
      puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU    "
      val = puzzle_to_lists(puzzle)
      self.assertListEqual(checkRowBackwards(val, "VIM"), [1,4])
    def test_check_Row_Backwards1(self):
      puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU    "
      val = puzzle_to_lists(puzzle)
      self.assertFalse(checkRowBackwards(val, "YO)))))))))"))
    def test_check_Diagonal(self):
       puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU    "
       val = puzzle_to_lists(puzzle)
       self.assertListEqual(checkDiagonal(val, "CPE"), [1,0])
    def test_check_Diagonal_1(self):
       puzzle = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU    "
       val = puzzle_to_lists(puzzle)
       self.assertFalse(checkDiagonal (val, "YEEHAW"))
if __name__ == '__main__':
   unittest.main()
