from solverFuncs import *
#Project 3
#Tushar Sharma
#Instructor: Julie Workman
puzzle = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
cages = get_cages()
checks = 0
row = 0
col = 0
backtracks = 0
square = 0
while square < 25:
  row = square//5
  col = square%5
  puzzle[row][col]+=1
  checks+=1
  if check_valid(puzzle, cages) == True: 
     square +=1
  elif puzzle[row][col] == 5:
     while puzzle[row][col] == 5:
      backtracks += 1
      puzzle[row][col] = 0
      square -= 1
      row = square//5
      col = square%5
print()
print("---Solution---")
print()
col = 0
for row in range(0,5):
 s = ' '.join(map(str,puzzle[row]))
 print(s+ " ")
print()
print("checks:", checks, "backtracks:", backtracks)

 
