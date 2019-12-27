from funcs import *

def printPuzzle(puzzle):
   for row in range(10):
      res = []
      for col in range(10):
         res.append(puzzle[col])
      puzzle = puzzle[10:]
      print("".join(res))


puzzle = input("")
print("Puzzle:")
print()
printPuzzle(puzzle)
print()
puzzle = puzzle_to_lists(puzzle)
words = input("")
words = words.split()
for word in words:
   if checkRows(puzzle, word) != False:
      val = checkRows(puzzle, word)
      print("%s: (FORWARD) row: %d column: %d" % (word, val[0], val[1]))
   elif checkColumns(puzzle,word)!= False:
      val = checkColumns(puzzle,word)
      print("%s: (DOWN) row: %d column: %d" %(word, val[0], val[1]))
   elif checkDiagonal(puzzle, word)!= False:
      val = checkDiagonal(puzzle, word)
      print("%s: (DIAGONAL) row: %d column: %d" %(word, val[0], val[1]))
   elif checkRowBackwards(puzzle, word)!= False:
      val = checkRowBackwards(puzzle, word)
      print("%s: (BACKWARD) row: %d column: %d" %(word, val[0], val[1]))
   elif checkColumnsBackwards(puzzle, word)!= False:
      val = checkColumnsBackwards(puzzle,word)
      print("%s: (UP) row: %d column: %d" %(word, val[0], val[1]))
   else:
    print("%s: word not found" %word)
