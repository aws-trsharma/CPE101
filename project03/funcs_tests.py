from solverFuncs import *
puzzle = [[1,4,3,2,5],[2,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
cages = [[9,3,0,5,6],[7,2,1,2],[10,3,3,8,13],[14,4,4,9,14,19],[3,1,7],[8,3,10,11,16],[13,4,12,17,21,22],[5,2,15,20],[6,3,18,23,24]]
print(check_rows_valid(puzzle))
print(check_columns_valid(puzzle))
print(check_cage_valid(puzzle,cages))
print(check_valid(puzzle, cages))
print(puzzle)
